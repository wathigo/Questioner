""" Import the necessary module """
from flask import jsonify, make_response, request
from flask_restful import Resource
from ....utils.validators_schema import ReserveValidate

from ..models.models_reserve import ReserveRecord


class Reserve(ReserveRecord, Resource):
    """ class to post reserve record"""
    def __init__(self):
        self.rec = ReserveRecord()

    def post(self, id):
        """ Post endpoint for post reserve endpoint"""
        json_data = request.get_json()
        data, errors = ReserveValidate().load(json_data)
        if errors:
            return make_response(jsonify({"status" : 400,
                                          "Error": errors}), 400)
        reserve = json_data['status']
        response = self.rec.create_reserve_record(id, reserve)
        if not response:
            return make_response(jsonify({"status" : 400,
                                          "Error": "Alredy reserved!"}), 201)
        return make_response(jsonify({"status" : 201,
                                      "data": response}), 201)
