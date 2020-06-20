from flask_restplus import Api
from flask import Blueprint
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

from .index import api as index

# db = SQLAlchemy()
# flask_bcrypt = Bcrypt()

api_bluePrint = Blueprint('api', __name__)

api = Api(api_bluePrint,
          title='CSV Consumer API',
          version='1.0',
          description='API service'
          )

api.add_namespace(index, path='/server/start')
