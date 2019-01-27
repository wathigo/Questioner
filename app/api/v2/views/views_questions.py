""" import the necessary modules """
from flask import jsonify, make_response, request
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity
from ....utils.validators_schema import QuestionValidate

from ..models.models_question import QuestionRecord

class Questions(QuestionRecord, Resource):
    """ Class to implement question endpont """
    def __init__(self):
        self.question_models = QuestionRecord()

    @jwt_required
    def post(self, id):
        """ post question request endpoint implementation"""
        json_data = request.get_json()
        data, errors = QuestionValidate().load(json_data)
        if errors:
            return make_response(jsonify({"status" : 400,
                                          "Error": errors}), 400)
        email = get_jwt_identity()
        response = self.question_models.create_record(id, json_data, email)
        if response == 'f':
            return make_response(jsonify({"status" : 400,
                                          "Error": "A question with the \
                                          given credentials exists!"}), 400)
        if not response:
            return make_response(jsonify({"status" : 400,
                                          "Error": "meetup record does not exists!"}), 400)

        return make_response(jsonify({"status" : 201,
                                      "data": response}), 201)

class Upvotes(QuestionRecord, Resource):
    """ Upvote a question endpoint """
    def __init__(self):
        self.models = QuestionRecord()

    @jwt_required
    def patch(self, id):
        """ upvote question endpoint implementation """
        response = self.models.vote(id, True)
        if not response:
            return make_response(jsonify({"status" : 404,
                                          "Error": "The question record \
                                          could not be retrieved!"}), 404)
        return make_response(jsonify({"status" : 201,
                                      "data": response}), 201)


class Downvotes(Upvotes):
    """ downvote a question record """
    def __init__(self):
        super(Downvotes, self).__init__()

    @jwt_required
    def patch(self, id):
        """ downvote question endpoint implementation """
        response = self.models.vote(id, False)
        if not response:
            return make_response(jsonify({"status" : 404,
                                          "Error": "The question record \
                                          could not be retrieved!"}), 404)
        return make_response(jsonify({"status" : 201,
                                      "data": response}), 201)
