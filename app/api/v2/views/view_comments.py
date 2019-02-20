""" import third party modules """
from flask import jsonify, make_response, request
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity
""" local imports"""
from ..models.models_comments import CommentsRecord
from ....utils.validators_schema import CommentValidate


class Comment(CommentsRecord, Resource):
    def __init__(self):
        self.models = CommentsRecord()

    @jwt_required
    def post(self, id):
        """ post comment endpoint implementation"""
        json_data = request.get_json()
        data, errors = CommentValidate().load(json_data)
        if errors:
            return make_response(jsonify({"status" : 400,
                                          "Error": errors}), 400)

        email = get_jwt_identity()
        response = self.models.create_comment_record(json_data, id, email)
        return make_response(jsonify({"status" : 201,
                                      "data": response}), 201)

    def get(self, id):
        """ endpoint to retrieve all the comments with a specific question id"""
        response = self.models.retrive_records(id)
        if response == []:
            return make_response(jsonify({"status" : 404,
                                          "Message": "No comments for this question exists!"}), 404)
        return make_response(jsonify({"status" : 200,
                                      "data": response}), 200)
