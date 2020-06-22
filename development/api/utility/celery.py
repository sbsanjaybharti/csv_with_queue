#!/usr/bin/env python3
"""
Import packages
"""
import os
from flask import Flask

from flask_sqlalchemy import SQLAlchemy
from ..config import config_by_name
from celery import Celery
from ..service.dataProcessService import DataProcess


def make_celery(app):
    """
    Configure the celery with RabbitMQ
    :param data:
    :return:
    """
    celery = Celery(
        app.import_name,
        backend='rpc://',
        broker='amqp://**:rabbitmq@rabbit1:5672/'
    )
    celery.conf.update(app.config)

    class ContextTask(celery.Task):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return self.run(*args, **kwargs)

    celery.Task = ContextTask
    return celery


app = Flask(__name__, instance_relative_config=True)
app.config.from_object(config_by_name[os.getenv('FLASK_CONFIG') or 'development'])

db = SQLAlchemy()
db.init_app(app)

celery = make_celery(app)


@celery.task(name='celery.task.data')
def dataCreate(data):
    """
    Send data to queue from celery
    :param data:
    :return:
    """
    process = DataProcess()
    process.process_start(data)


def data_upload_queue(data):
    """
    Send data to queue
    :param data:
    :return:
    """
    process = DataProcess()
    process.process_start(data)
