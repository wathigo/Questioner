""" Import the necessary module """
from flask import jsonify, make_response, request
from flask_restful import Resource
from ....utils.validators import Views

from ..models.models_reserve import ReserveRecord


class Reserve(ReserveRecord, Resource):
    """ class to post reserve record"""
    def __init__(self):
        self.rec = ReserveRecord()
        self.validate = Views()

    def post(self, id):
        """ Post endpoint for post reserve endpoint"""
        data = request.get_json()
        valid = self.validate.validate_reserve_keys(data)
        if valid:
            return make_response(jsonify({"status" : 400,
                                          "Error": valid}), 400)
        reserve = data['status']
        response = self.rec.create_reserve_record(id, reserve)
        return make_response(jsonify({"status" : 201,
                                      "data": response}), 201)
