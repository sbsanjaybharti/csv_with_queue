#!/usr/bin/env python3
"""
Import packages
"""
from flask_restplus import Resource, Namespace, reqparse
import werkzeug
from .utility.file import files
from .utility.celery import dataCreate, data_upload_queue

api = Namespace('Files', description='file uploading')

# Set parameter for file upload
file_upload = reqparse.RequestParser()
file_upload.add_argument('file',
                         type=werkzeug.datastructures.FileStorage,
                         location='files',
                         required=True,
                         help='CSV file only')


@api.route('/')
class file(Resource):
    """
    Used to upload file
    """

    @api.expect(file_upload)
    def post(self):
        """
         API for uploading CSV data file
         ## Implementation Notes
         __Note__ : No limit for file size, Data
         1. Data cleaning will te taken care by Panda library
         2. Data transfer to database will be done by rabbitMQ
            with celery to reduce load and user waiting time.

        """
        args = file_upload.parse_args()
        file_obj = files(args['file'])

        response = file_obj.upload()

        try:
            # ********************************************
            # Celery call for process the file
            # ********************************************

            # dataCreate.delay(response['file_name'])
            data_upload_queue(response['file_name'])

            # ********************************************
            # Celery call for process the file
            # ********************************************
        except Exception as e:
            response_object = {
                'code': 500,
                'type': 'Internal Server Errors',
                'message': 'Exception occur in task service, Try again later!',
            }
            return response_object

        return response
