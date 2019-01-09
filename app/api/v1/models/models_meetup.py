import datetime
meetup_rec = []

class MeetupRecord():
    def __init__(self):
        self.mettup_records = meetup_rec

    def save(self, title, description):
        data = {
        "createdOn" : datetime.datetime.now(),
        "id" : len(meetup_rec)+1,
        "Title": title,
        "Description": description
        }
        meetup_rec.append(data)
        return meetup_rec

    def get_items(self):
        return meetup_rec

    def get_item(self, item_id):
        item = None
        for record in meetup_rec:
            if record['id'] == item_id:
                item = record
        return item
