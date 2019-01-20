""" import the necessary modules """
import datetime
from .models_base import BaseModels


class ReserveRecord(BaseModels):
    """Models for reserve record."""
    def __init__(self):
        self.record = BaseModels('reserve')

    def create_reserve_record(self, meetup_id, reserve):
        """ Create a new reserve record """
        data = {
            "meetup_id" : meetup_id,
            "reserved_on" : datetime.datetime.now(),
            "status" : reserve
        }
        self.record.save(data)
        return data
