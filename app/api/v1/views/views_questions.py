""" import the necessary modules """
from flask import jsonify, make_response, request
from flask_restful import Resource
from ....utils.validators import Views

from ..models.models_question import QuestionRecord

class Questions(QuestionRecord, Resource):
    """ Class to implement question endpont """
    def __init__(self):
        self.question_models = QuestionRecord()
        self.validate = Views()

    def post(self, id):
        """ post question request endpoint implementation"""
        data = request.get_json()
        valid = self.validate.validate_question_keys(data)
        if valid:
            return make_response(jsonify({"status" : 400,
                                          "Error": valid}), 400)
        question = data['question']
        response = self.question_models.create_record(id, question)
        if response is not None:
            return make_response(jsonify({"status" : 201,
                                          "data": response}), 201)
        return make_response(jsonify({"status" : 500,
                                      "Error": "Record could not be created"}), 500)


class Upvotes(QuestionRecord, Resource):
    """ Upvote a question endpoint """
    def __init__(self):
        self.models = QuestionRecord()

    def patch(self, id):
        """ upvote question endpoint implementation """
        response = self.models.vote(id, True)
        if not response:
            return make_response(jsonify({"status" : 404,
                                          "Error": "Question record not found!"}), 201)
        return make_response(jsonify({"status" : 201,
                                      "data": response}), 201)


class Downvotes(Upvotes):
    """ downvote a question record """
    def __init__(self):
        super(Downvotes, self).__init__()

    def patch(self, id):
        """ downvote question endpoint implementation """
        response = self.models.vote(id, False)
        return make_response(jsonify({"status" : 201,
                                      "data": response}), 201)
