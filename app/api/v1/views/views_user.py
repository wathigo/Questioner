""" import the necessary modules """
from flask import jsonify, make_response, request
from flask_restful import Resource
from ..models.models_user import UserRecord
from ....utils.validators_schema import UserValidate



class Users(UserRecord, Resource):
    """User record endpoints"""
    def __init__(self):
        self.record = UserRecord()

    def post(self):
        """ post endpoint for user registration """
        json_data = request.get_json()
        data, errors = UserValidate().load(json_data)
        if errors:
            return make_response(jsonify({"status" : 400,
                                          "Error": errors}), 400)
        if json_data['Password'] != json_data['RepeatPassword']:
            return make_response(jsonify({"status" : 400,
                                          "Error": "Passwords does not match!"}), 400)
        response = self.record.create_user(json_data)
        return make_response(jsonify({"status" : 201, "data": response}), 201)


class UserLogin(UserRecord, Resource):
    """ class to login a user """
    def __init__(self):
        self.models = UserRecord()

    def post(self):
        """ post request endpoint for user login """
        data = request.get_json()
        user = self.models.authenticate_user(data)
        if not user:
            return make_response(jsonify({"status" : 404,
                                          "Error": "User not found"}), 404)
        if user == 'f':
            return make_response(jsonify({"status" : 400,
                                          "Message": "Password does not match!"}), 400)
        return make_response(jsonify({"status" :200,
                                      "Message": user}), 200)
