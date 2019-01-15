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
        responce = self.rec.save(title, description, date, location)
        return make_response(jsonify({"status" : 201,
                                      "My new meetup records are": responce}), 201)

    def get(self):
        """ get endpoint to get all the records """
        data = self.rec.get_items()
        return make_response(jsonify({"status": 200,
                                      "My meetup records are": data}), 200)


class Meetups(MeetupRecord, Resource):
    """ enpoints to route with a meetup id """
    def __init__(self):
        self.rec = MeetupRecord()

    def get(self, id):
        """ get endpoint to get a specific meetup record """
        item = self.rec.get_item(id)
        if item is not None: ### item found
            return make_response(jsonify({"status" : 200,
                                          "My meetup record is": item}), 200)
        else:
            return make_response(jsonify({"status" : 404,
                                          "Message": "Item not found!"}), 404)

    def put(self, id):
        data = request.get_json()
        item = self.rec.get_item(id)
        if item is None: ### item not found
            return make_response(jsonify({"status" : 404,
                                          "Message": "Item not found!"}), 404)
        item['Title'] = data['Title']
        item['Description'] = data['Description']
        item['Date'] = data['Date']
        item['Location'] = data['Location']
        return make_response(jsonify({"status" : 200,
                                      "Record updated successfully": item}), 200)
