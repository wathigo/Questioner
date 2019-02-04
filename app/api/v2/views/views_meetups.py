""" import third party modules """
from flask import jsonify, make_response, request
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity
""" Local imports """
from ....utils.validators_schema import MeetupValidate
from ..models.models_meetup import MeetupRecord

class Meetup(MeetupRecord, Resource):
    """ enpoints to route without a meetup id """
    def __init__(self):
        self.rec = MeetupRecord()

    @jwt_required
    def post(self):
        """ post endpoint for meetup record creation """
        data = request.get_json()
        data, errors = MeetupValidate().load(data)
        if errors:
            return make_response(jsonify({"status" : 400,
                                          "Error": errors}), 400)
        email = get_jwt_identity()
        response = self.rec.create_record(data, email)
        if not response:
            return make_response(jsonify({"status" : 401,
                                          "Message": "Only Admin users \
                                          are allowed to create a meetup!"}), 401)
        if response == 'f':
            return make_response(jsonify({"status" : 400,
                                          "Error": "Meetup matching the credentials given exists!"}), 400)
        return make_response(jsonify({"status" : 201,
                                      "data": response}), 201)

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
        self.record = MeetupRecord()


    def get(self, id):
        """ get endpoint to get a specific meetup record """
        item = self.record.get_item(id)
        if item: ### item found
            return make_response(jsonify({"status" : 200,
                                          "data": item}), 200)
        return make_response(jsonify({"status" : 404,
                                      "Message": "Item not found!"}), 404)
    @jwt_required
    def delete(self, id):
        """ Endpoint to delete a meetup"""
        email = get_jwt_identity()
        response = self.record.delete_item(email, id)
        if not response:
            return make_response(jsonify({"status" : 401,
                                          "Message": "Only admins are \
                                           allowed to delete a meetup!"}), 401)
        if response == 'f':
            return make_response(jsonify({"status" : 404,
                                          "Message": "Item not found!"}), 404)
        return make_response(jsonify({"status" : 200,
                                      "data": "item deleted"}), 200)
