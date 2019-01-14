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
        data = request.get_json()
        valid = self.validate.validate_reserve_keys(data)
        if not valid:
            return make_response(jsonify({"status" : 400,
                                          "Error": "Invalid key"}), 400)
        reserve = data['status']
        response = self.rec.save(id, reserve)
        return make_response(jsonify({"status" : 201,
                                      "My new reserve records are": response}), 201)
