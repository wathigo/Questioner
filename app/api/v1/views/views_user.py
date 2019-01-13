""" import the necessary modules """
from flask import jsonify, make_response, request
from flask_restful import Resource
from ..models.models_user import UserRecord
from ....utils.validators import Views


class Users(UserRecord, Resource):
    """User record endpoints"""
    def __init__(self):
        self.rec = UserRecord()
        self.validate = Views()

    def post(self):
        """ post endpoint for user registration """
        data = request.get_json()
        valid = self.validate.validate_user(data)
        if valid:
            return make_response(jsonify({"Error": valid}), 400)
        fname = data['FirstName']
        lname = data['LastName']
        email = data['Email']
        password = data['Password']
        response = self.rec.save(fname, lname, email, password)
        return make_response(jsonify({"My new meetup records are": response}), 201)
