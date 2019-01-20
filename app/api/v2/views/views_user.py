""" import the necessary modules """
from flask import jsonify, make_response, request
from flask_restful import Resource
from ..models.models_user import UserRecord
from ....utils.validators_schema import UserValidate


class Users(UserRecord, Resource):
    """User record endpoints"""
    def __init__(self):
        self.rec = UserRecord()

    def post(self):
        """ post endpoint for user registration """
        data = request.get_json()
        data, errors = UserValidate().load(data)
        if errors:
            return make_response(jsonify({"status" : 400,
                                          "Error": errors}), 400)
        fname = data['FirstName']
        lname = data['LastName']
        email = data['Email']
        password = data['Password']
        response = self.rec.save(fname, lname, email, password)
        return make_response(jsonify({"status" : 201,
                                      "data": response}), 201)
