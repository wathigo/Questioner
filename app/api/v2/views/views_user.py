""" import the necessary modules """
from flask import jsonify, make_response, request
from flask_restful import Resource
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
        response = self.models.create_user(json_data)
        return make_response(jsonify({"status" : 201,
                                      "data": response}), 201)

class UserLogin(UserRecord, Resource):
    """ Class to authenticate a user"""
    def __init__(self):
        self.models = UserRecord()
    def post(self):
        """ endpoint for user login"""
        json_data = request.get_json()
        response = self.models.authenticate_user(json_data)
