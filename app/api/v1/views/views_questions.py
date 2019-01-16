from flask import jsonify, make_response, request
from flask_restful import Resource
from app.api.v1 import version_one as v1
from ..models.models_meetup import MeetupRecord
from ....utils.validators import Views

from ..models.models_question import QuestionRecord

class Questions(QuestionRecord, Resource):
    def __init__(self):
        self.question_models = QuestionRecord()
        self.validate = Views()

    def post(self, id):
        data = request.get_json()
        valid = self.validate.validate_question_keys(data)
        if valid:
            return make_response(jsonify({"status" : 400,
                                          "Error": valid}), 400)
        question = data['question']
        response = self.question_models.save(id, question)
        if response is not None:
            return make_response(jsonify({"status" : 201,
                                          "data": response}), 201)
        return make_response(jsonify({"status" : 500,
                                      "Error": "Record could not be created"}), 500)
