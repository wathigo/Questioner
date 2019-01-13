""" import the necessary modules"""
from flask_restful import Api
from flask import Blueprint

version_one = Blueprint('api_v1', __name__, url_prefix='/api/v1')
api = Api(version_one)
from .views.views_meetups import Meetup, Meetups
from .views.views_questions import Questions
from .views.views_votes import Upvotes, Downvotes
from .views.views_reserve import Reserve
from .views.views_user import Users

api.add_resource(Users, '/auth/signup')
api.add_resource(Meetup, '/meetups')
api.add_resource(Meetups, '/meetups/<int:id>')
api.add_resource(Reserve, '/meetups/<int:id>/rsvps')
api.add_resource(Questions, '/meetups/<int:id>/questions')
api.add_resource(Upvotes, '/questions/<int:id>/upvote')
api.add_resource(Downvotes, '/questions/<int:id>/downvote')
