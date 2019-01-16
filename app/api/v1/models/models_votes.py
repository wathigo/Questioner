import datetime

votes_records = []

class VotesRecord():
    def __init__(self):
        self.rec = votes_records

    def find(self, id):
        response = None
        for item in self.rec:
            if item['meetup_id'] == id:
                response = item
        return response

    def save(self, id, vote):
        ### True arguement is for an Upvote
        data = {
            "meetup_id" : id,
            "votes" : 0,
            "voted_on" : datetime.datetime.now()
        }
        ### True arguement is for an Upvote
        if vote:
            data['votes'] = data['votes'] + 1
            ### False arguement is for an downvote
        elif data['votes'] > 1:
            data['downvotes'] = data['downvotes'] - 1
        self.rec.append(data)
        return self.rec

    def vote(self, id, vote):
        record = self.find(id)
        if record is not None:  ### Record exists...
            if vote:
                record['votes'] = record['votes'] + 1
            elif record['votes'] > 1:
                record['votes'] = record['votes'] - 1
            return record
        else: ### record does not exists
            response = self.save(id, vote)
        return response
