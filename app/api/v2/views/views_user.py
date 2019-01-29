""" import the necessary modules """
from flask import jsonify, make_response, request
from flask_restful import Resource
import datetime
from flask_jwt_extended import create_access_token, create_refresh_token
from ..models.models_user import UserRecord
from ....utils.validators_schema import UserValidate


class Users(UserRecord, Resource):
    """User record endpoints"""
    def __init__(self):
        self.models = UserRecord()

    def post(self):
        """ post endpoint for user registration """
        json_data = request.get_json()
        data, errors = UserValidate().load(json_data)
        if errors:
            return make_response(jsonify({"status" : 400,
                                          "Error": errors}), 400)
        response = self.models.create_user(json_data, False)
        time = datetime.timedelta(days=2)
        access_token = create_access_token(identity=json_data['email'], expires_delta=time)
        if response is 'f':
            return make_response(jsonify({"status" : 400,
                                          "Message": "Password does not match!"}), 400)
        if response is False:
            return make_response(jsonify({"status" : 400,
                                          "Message": "A user with the given Email exists"}), 400)
        return make_response(jsonify({"status" : 201,
                                      "message" : "Logged in as{}".\
                                      format(response['email'].split("@")[0]),
                                      "access_token" : access_token,
                                      "data": response}), 201)


class AdminSignup(Users, Resource):
    """Admin Admin signup endpoint"""
    def __init__(self):
        self.models = UserRecord()

    def post(self):
        """ post endpoint for user registration """
        json_data = request.get_json()
        data, errors = UserValidate().load(json_data)
        if errors:
            return make_response(jsonify({"status" : 400,
                                          "Error": errors}), 400)
        response = self.models.create_user(json_data, True)
        if not response:
            return make_response(jsonify({"status" : 400,
                                          "Message": "A user with the given Email exists"}), 400)
        time = datetime.timedelta(days=2)
        access_token = create_access_token(identity=response['email'], expires_delta=time)
        return make_response(jsonify({"status" : 201,
                                      "message" : "Logged in as{}".\
                                      format(response['email'].split("@")[0]),
                                      "access_token" : access_token,
                                      "data": response}), 201)

class UserLogin(UserRecord, Resource):
    """ Class to authenticate a user"""
    def __init__(self):
        self.models = UserRecord()

    def post(self):
        """ endpoint for user login"""
        json_data = request.get_json()
        response = self.models.authenticate_user(json_data)
        if response == 'f':
            return make_response(jsonify({"status" : 404,
                                          "Error": "User does not exists!"}), 404)
        elif response is False:
            return make_response(jsonify({"status" : 400,
                                          "Error": "Wrong username/password!"}), 400)
        time = datetime.timedelta(days=2)
        access_token = create_access_token(identity=json_data['email'], expires_delta=time)
        return make_response(jsonify({"status" : 200,
                                      "Message": "Logged in as {}"\
                                      .format(json_data['email'].split("@")[0]),
                                      "access_token" : access_token}), 200)
