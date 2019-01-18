""" import the necessary modules """
from flask import jsonify, make_response, request
from flask_restful import Resource
from ....utils.validators import Views
from ..models.models_meetup import MeetupRecord

class Meetup(MeetupRecord, Resource):
    """ enpoints to route without a meetup id """
    def __init__(self):
        self.rec = MeetupRecord()
        self.validate = Views()

    def post(self):
        """ post endpoint for meetup record creation """
        data = request.get_json()
        valid = self.validate.validate_meetups(data)
        if valid:
            return make_response(jsonify({"status" : 400,
                                          "Error": valid}), 400)
        title = data['Title']
        description = data['Description']
        date = data['Date']
        location = data['Location']
        responce = self.rec.create_record(title, description, date, location)
        return make_response(jsonify({"status" : 201,
                                      "data": responce}), 201)

class MeetupsUpcoming(MeetupRecord, Resource):
    """ enpoints to get the upcoming meetups """
    def __init__(self):
        self.rec = MeetupRecord()

    def get(self):
        """ get endpoint to get all the the upcoming meetups """
        data = self.rec.get_items()
        return make_response(jsonify({"status": 200,
                                      "data": data}), 200)


class Meetups(MeetupRecord, Resource):
    """ enpoints to route with a meetup id """
    def __init__(self):
        self.rec = MeetupRecord()

    def get(self, id):
        """ get endpoint to get a specific meetup record """
        item = self.rec.get_item(id)
        if item: ### item found
            return make_response(jsonify({"status" : 200,
                                          "data": item}), 200)
        return make_response(jsonify({"status" : 404,
                                      "Message": "Item not found!"}), 404)

    def put(self, id):
        """ Update a specific meetup """
        data = request.get_json()
        item = self.rec.get_item(id)
        if item is False: ### item not found
            return make_response(jsonify({"status" : 404,
                                          "Message": "Item not found!"}), 404)
        item[0]['Title'] = data['Title']
        item[0]['Description'] = data['Description']
        item[0]['Date'] = data['Date']
        item[0]['Location'] = data['Location']
        return make_response(jsonify({"status" : 200,
                                      "data": item}), 200)
