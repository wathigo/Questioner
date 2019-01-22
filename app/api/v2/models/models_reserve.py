""" import the necessary modules """
import datetime
from .models_base import BaseModels


class ReserveRecord(BaseModels):
    """Models for reserve record."""
    def __init__(self):
        self.record = BaseModels('reserve')

    def create_reserve_record(self, meetup_id, reserve):
        """ Create a new reserve record """
        meetup = BaseModels('meetups')
        exists = meetup.check_exists('meetupid', meetup_id)
        if not exists:
            return False
        data = {
            "meetup_id" : meetup_id,
            "status" : reserve
        }
        query = """INSERT INTO reserve(meetupid, response)
        VALUES ('%s', '%s')""" % \
        (data['meetup_id'], data['status'])
        self.record.save(query, data)
        return data
