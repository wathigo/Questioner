from flask import jsonify, make_response, request
from flask_restful import Resource
from app.api.v1 import version_one as v1

from ..models.models_question import QuestionRecord

class Questions(QuestionRecord, Resource):
    def __init__(self):
        self.question_models = QuestionRecord()

    def post(self, id):
        data = request.get_json()
        question = data['question']
        response = self.question_models.save(id, question)
        if response is not None:
            return make_response(jsonify({"My new question records are": response}), 201)
        return make_response(jsonify({"Error": "Record could not be created"}), 500)
