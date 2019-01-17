""" Import the necessary modules """
import os
from flask import Flask, Blueprint
from instance.config import app_config
from .utils.database import create_tables
from .api.v1 import version_one as v1

def create_app():
    """ Create the app """
    app = Flask(__name__)
    app.register_blueprint(v1)
    config_env = os.environ.get('FLASK_ENV')
    app.config.from_object(app_config[config_env])
    create_tables()

    return app
