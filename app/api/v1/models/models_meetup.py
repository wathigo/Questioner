import datetime
MEETUP_RECORD = []

class MeetupRecord():
    def __init__(self):
        self.meetup_records = MEETUP_RECORD

    def save(self, title, description, date, location):
        data = {
            "createdOn" : datetime.datetime.now(),
            "id" : len(self.meetup_records)+1,
            "Title": title,
            "Description": description,
            "Date" : date,
            "Location" : location
            }
        self.meetup_records.append(data)
        return self.meetup_records

    def get_items(self):
        return self.meetup_records

    def get_item(self, item_id):
        item = None
        for record in self.meetup_records:
            if record['id'] == item_id:
                item = record
        return item
