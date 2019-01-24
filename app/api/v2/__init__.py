""" import the necessary modules"""
from flask_restful import Api
from flask import Blueprint

version_two = Blueprint('api_v2', __name__, url_prefix='/api/v2')
api = Api(version_two)
""" import classes containg the endpoints """
from .views.views_meetups import Meetup, Meetups, MeetupsUpcoming
from .views.views_questions import Questions, Upvotes, Downvotes
from .views.views_reserve import Reserve
from .views.views_user import Users, UserLogin, AdminSignup

api.add_resource(Users, '/auth/signup')
api.add_resource(AdminSignup, '/auth/admin/signup')
api.add_resource(UserLogin, '/auth/login')
api.add_resource(Meetup, '/meetups')
api.add_resource(MeetupsUpcoming, '/meetups/upcoming')
api.add_resource(Meetups, '/meetups/<int:id>')
api.add_resource(Reserve, '/meetups/<int:id>/rsvps')
api.add_resource(Questions, '/meetups/<int:id>/questions')
api.add_resource(Upvotes, '/questions/<int:id>/upvote')
api.add_resource(Downvotes, '/questions/<int:id>/downvote')
