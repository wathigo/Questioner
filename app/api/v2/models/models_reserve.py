""" import the necessary modules """
import datetime
from .models_base import BaseModels


class ReserveRecord(BaseModels):
    """Models for reserve record."""
    def __init__(self):
        self.record = BaseModels('reserve')

    def create_reserve_record(self, meetup_id, reserve, email):
        """ Create a new reserve record """
        user = BaseModels('user_table')
        user_record = user.find('email', email)
        if user_record is None:
            return 'f'
        userid = user_record['userid']
        meetup = BaseModels('meetups')
        exists = meetup.check_exists('meetupid', meetup_id)
        if not exists:
            return False
        data = {
            "userid" : userid,
            "meetup_id" : meetup_id,
            "status" : reserve
        }
        query = """INSERT INTO reserve(userid, meetupid, response)
        VALUES ('%s', '%s', '%s')""" % \
        (data['userid'], data['meetup_id'], data['status'])
        self.record.save(query, data)
        return data
