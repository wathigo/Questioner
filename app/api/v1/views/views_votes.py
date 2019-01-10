from flask import jsonify, make_response, request
from flask_restful import Resource
from app.api.v1 import version_one as v1

from ..models.models_votes import VotesRecord

class Upvotes(VotesRecord, Resource):
    def __init__(self):
        self.rec = VotesRecord()

    def patch(self, id):
        response = self.rec.upvote(id)
        return make_response(jsonify({"My updated votes records are": response}), 201)


class Downvotes(VotesRecord, Resource):
    def __init__(self):
        self.rec = VotesRecord()

    def patch(self, id):
        response = self.rec.downvote(id)
        return make_response(jsonify({"My updated votes records are": response}), 201)
