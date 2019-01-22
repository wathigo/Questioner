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
        return self.records.return_record()

    def get_item(self, item_id):
        """ get a specific item """
        found = False
        item = self.records.find('meetupid', item_id)
        if item:
            found = item
        return found
