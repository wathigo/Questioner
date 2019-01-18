import datetime

RESERVE_RECORD = []

class ReserveRecord():
    """Models for reserve record."""
    def __init__(self):
        self.records = RESERVE_RECORD

    def save(self, id, reserve):
        data = {
            "meetup_id" : id,
            "reserved_on" : datetime.datetime.now(),
            "status" : reserve
        }
        self.records.append(data)
        return data