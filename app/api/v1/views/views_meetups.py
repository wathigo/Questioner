from flask import jsonify, make_response, request
from flask_restful import Resource
from app.api.v1 import version_one as v1
from ..models.models_meetup import MeetupRecord

class Meetup(MeetupRecord, Resource):
    def __init__(self):
        self.rec = MeetupRecord()

    def post(self):
        data = request.get_json()
        title = data['Title']
        description = data['Description']
        responce = self.rec.save(title, description)
        return make_response(jsonify({"My new meetup records are": responce}), 201)

    def get(self):
        data = self.rec.get_items()
        return make_response(jsonify({"My meetup records are": data}), 200)


class Meetups(MeetupRecord, Resource):
    def __init__(self):
        self.rec = MeetupRecord()

    def get(self, id):
        item = self.rec.get_item(id)
        if item is not None:
            return make_response(jsonify({"My meetup record is": item}), 200)
        else:
            return make_response(jsonify({"Error": "Item not found!"}))
