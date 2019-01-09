meetup_rec = []

class MeetupRecord():
    def __init__(self):
        self.mettup_records = meetup_rec

    def save(self, title, description):
        data = {
        "Title": title,
        "Description": description
        }
        meetup_rec.append(data)
        return meetup_rec
