from flask import jsonify, make_response, request
from flask_restful import Resource
from app.api.v1 import version_one as v1

from ..models.models_votes import VotesRecord

class Upvotes(VotesRecord, Resource):
    def __init__(self):
        self.rec = VotesRecord()

    def patch(self, id):
        response = self.rec.vote(id, True)
        return make_response(jsonify({"My updated votes records are": response}), 201)


class Downvotes(Upvotes, VotesRecord, Resource):
    def __init__(self):
        super(Downvotes, self).__init__()

    def patch(self, id):
        response = self.rec.vote(id, False)
        return make_response(jsonify({"My updated votes records are": response}), 201)
