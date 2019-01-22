""" local imports """
from .models_base import BaseModels

class MeetupRecord(BaseModels):
    """ Constructor that calls the Constructor in BaseModels"""
    def __init__(self):
        self.records = BaseModels('meetups')

    def create_record(self, data):
        """ create a new meetup record """
        data = {
            "Title": data['Title'],
            "Description": data['Description'],
            "Date" : data['Date'],
            "Location" : data['Location']
            }
        query = """INSERT INTO meetups(title, description, location, happeningon)
        VALUES ('%s', '%s', '%s', '%s');""" % \
        (data['Title'], data['Description'], data['Location'], data['Date'])
        record = self.records.save(query, data)
        return record

    def get_items(self):
        """ Return the whole database"""
        response = []
        data = self.records.return_record()
        for item in data:
            record = self.modify_response(item)
            response.append(record)
        return response

    def modify_response(self, data):
        """ Method to modify meetup response"""
        response = {
            "Title" : data[1],
            "Description" : data[2],
            "Venue" : data[3],
            "Date" : data[4]
            }
        return response

    def get_item(self, item_id):
        """ get a specific item """
        found = False
        item = self.records.find('meetupid', item_id)
        if item:
            response = []
            record = self.modify_response(item)
            response.append(record)
            found = response
        return found
