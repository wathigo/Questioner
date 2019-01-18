""" import datetime module """
import datetime
from .models_base import BaseModels

class MeetupRecord(BaseModels):
    """ Contructor that calls the Constructor in BaseModels"""
    def __init__(self):
        self.records = BaseModels('meetup')

    def create_record(self, title, description, date, location):
        """ create a new meetup record """
        data = {
            "createdOn" : datetime.datetime.now(),
            "id" : self.records.check_record_size()+1,
            "Title": title,
            "Description": description,
            "Date" : date,
            "Location" : location
            }
        record = self.records.save(data)
        return record

    def get_items(self):
        """ Return the whole data structure"""
        return self.records.return_record()

    def get_item(self, item_id):
        """ get a specific item """
        found = False
        item = self.records.find('id', item_id)
        if item:
            found = item
        return found
