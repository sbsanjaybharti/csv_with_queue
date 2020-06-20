import os
from flask import jsonify
from flask_restplus import Resource, Namespace
from .utility.rabbit_mq import RabbitMq

api = Namespace('Consumer', description='Insert data')


@api.route('/')
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
