#!/usr/bin/env python3
"""
Import packages
"""
import unittest
from flask import Flask
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from api.config import config_by_name
# from api import *
from api import api_bluePrint
from api.main import db, flask_bcrypt

#############################################################################
# Setting Flask
# Setting configuration for production development and testing
#############################################################################
app = Flask(__name__)
app.config.from_object(config_by_name['development'])
db.init_app(app)
flask_bcrypt.init_app(app)
app.register_blueprint(api_bluePrint)

# Migration setting for CLI
app.app_context().push()
manager = Manager(app)
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)

#############################################################################
# Command: python run.py run
# To run the application
#############################################################################
@manager.command
def run():
    """
    Command: python run.py run
    Description: To run the application
    """
    app.run()

#############################################################################
# Command: python run.py test
# Use to run Unit test
#############################################################################
@manager.command
def test():
    """Runs the unit tests."""
    tests = unittest.TestLoader().discover('test', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1

if __name__ == "__main__":
    manager.run()
