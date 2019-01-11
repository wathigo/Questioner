from flask import jsonify, make_response, request
from flask_restful import Resource
from app.api.v1 import version_one as v1

from ..models.models_reserve import ReserveRecord


class Reserve(ReserveRecord, Resource):
    def __init__(self):
        self.rec = ReserveRecord()

    def post(self, id):
        data = request.get_json()
        reserve = data['reserve']
        response = self.rec.save(id, reserve)
        return make_response(jsonify({"My new reserve records are": response}), 201)
