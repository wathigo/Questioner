""" Import the necessary modules """
import os
from flask_jwt_extended import JWTManager
from flask import Flask, Blueprint
from instance.config import app_config
from .utils.database import create_tables, insert_data
from .api.v1 import version_one as v1
from .api.v2 import version_two as v2


def create_app():
    """ Create the app """
    app = Flask(__name__)
    app.register_blueprint(v1)
    app.register_blueprint(v2)
    os.environ['FLASK_ENV'] = 'development'
    app.config.from_object(app_config['development'])
    app.config['JWT_SECRET_KEY'] = 'secret-string'
    jwt = JWTManager(app)
    create_tables()
    insert_data()


    return app
