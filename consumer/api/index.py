#!/usr/bin/env python3
"""
Import packages
"""
import os
from flask import jsonify, request
from flask_restplus import Resource, Namespace
from .utility.rabbit_mq import RabbitMq
from .service.dataProcessService import recordData

api = Namespace('Consumer', description='Insert data')


@api.route('/start')
class index(Resource):
    @api.doc('Start consuming')
    def get(self):
        """Home page"""
        server = RabbitMq()
        server.startserver()

        response_object = {
            'code': '200',
            'type': 'Response',
            'message': 'RadditMQ server started'
        }
        return jsonify(response_object)


@api.route('/list')
class List(Resource):
    @api.doc(params={'page': 'Pagination no. of page'})
    def get(self):
        """Display Records in Json"""

        args = request.args
        if 'page' in args and args['page'] is not None:
            page = args['page']
        else:
            page = 1

        result = recordData().list(page)
        response_object = {
            'code': '200',
            'type': 'Response',
            'message': 'List data successfully',
            'data': result
        }
        return jsonify(response_object)
