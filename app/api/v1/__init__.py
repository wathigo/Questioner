from flask_restful import Api
from flask import Blueprint

version_one = Blueprint('api_v1', __name__, url_prefix='/api/v1')
api = Api(version_one)

from .views.views_meetups import Meetup, Meetups
from .views.views_questions import Questions
api.add_resource(Meetup, '/meetups')
api.add_resource(Meetups, '/meetups/<int:id>')
api.add_resource(Questions, '/meetups/<int:id>/questions')
