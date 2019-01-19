""" import the necessary modules """
from flask import jsonify, make_response, request
from flask_restful import Resource
from ..models.models_user import UserRecord
from ....utils.validators import Views


class Users(UserRecord, Resource):
    """User record endpoints"""
    def __init__(self):
        self.record = UserRecord()
        self.validate = Views()

    def post(self):
        """ post endpoint for user registration """
        data = request.get_json()
        valid = self.validate.validate_user(data)
        if valid:
            return make_response(jsonify({"status" : 400,
                                          "Error": valid}), 400)
        fname = data['FirstName']
        lname = data['LastName']
        email = data['Email']
        password = data['Password']
        response = self.record.create_user(fname, lname, email, password)
        return make_response(jsonify({"status" : 201,
                                      "data": response}), 201)


class UserLogin(UserRecord, Resource):
    """ class to login a user """
    def __init__(self):
        self.rec = UserRecord()
        self.validate = Views()

    def post(self):
        """ post request endpoint for user login """
        data = request.get_json()
        valid = self.validate.validate_user_login(data)
        if valid:
            return make_response(jsonify({"status" : 400,
                                          "Error": valid}), 400)
        email = data['Email']
        password = data['Password']
        user = self.rec.authenticate_user(email, password)
        if not user:
            return make_response(jsonify({"status" : 404,
                                          "Error": "User not found"}), 404)
        if user == 'f':
            return make_response(jsonify({"status" : 400,
                                          "Message": "Password does not match!"}), 400)
        return make_response(jsonify({"status" :200,
                                      "Message": user}), 200)
