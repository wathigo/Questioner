""" local imports """
from flask import jsonify
from .models_base import BaseModels

class MeetupRecord(BaseModels):
    """ Constructor that calls the Constructor in BaseModels"""
    def __init__(self):
        self.records = BaseModels('meetups')

    def create_record(self, data, email):
        """ create a new meetup record """
        ### Get the userid
        user_record = BaseModels('user_table')
        user = user_record.find('email', email)
        if not user['isadmin']:
            return False
        title = self.records.find('title', data['title'])
        date = self.records.find('location', data['location'])
        if title and date:
            return 'f'
        userid = user['userid']
        data = {
            "userid" : userid,
            "title": data['title'],
            "description": data['description'],
            "date" : data['date'],
            "location" : data['location']
            }
        query = """INSERT INTO meetups(userid, title, description, location, happeningon)
        VALUES ('%s', '%s', '%s', '%s', '%s')
        RETURNING meetupid, title, description, location, happeningon, userid, createdon;""" % \
        (data['userid'], data['title'], data['description'], data['location'], data['date'])
        record = self.records.save(query)
        return record

    def get_items(self):
        """ Return the whole database"""
        query = """ SELECT json_build_object('meetupid', meetupid, 'title', title, 'description', \
        description, 'vanue', location, 'date', happeningon, 'user', userid) FROM (SELECT * FROM meetups)
        AS get_all;""".\
        format('meetups')
        data = self.records.return_record(query)
        return data

    def get_item(self, item_id):
        """ get a specific item """
        found = False
        query = """ SELECT json_build_object('meetupid', meetupid, 'title', title, 'description', \
        description, 'venue', location, 'date', happeningon, 'user', userid) FROM (SELECT * FROM meetups\
        WHERE meetupid = {})
        AS fetch_specific;""".\
        format(item_id)
        data = self.records.return_record(query)
        if data:
            found = data
        return found

    def delete_item(self, email, meetupid):
        user = BaseModels('user_table')
        user_data = user.find('email', email)
        isadmin = user_data['isadmin']
        if not isadmin:
            return False
        item = self.records.check_exists("meetupid", meetupid)
        if not item:
            return 'f'
        query = """DELETE FROM meetups WHERE meetupid='%s';""" % (meetupid)
        updated_records = self.records.delete(query)
        return updated_records
