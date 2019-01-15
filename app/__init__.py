""" Import the necessary modules """
from flask import Flask, Blueprint
from instance.config import app_config

from .api.v1 import version_one as v1

def create_app():
    """ Create the app """
    app = Flask(__name__)
    app.register_blueprint(v1)
    app.config.from_object(app_config)
    return app
