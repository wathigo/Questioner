import datetime

votes_records = []

class VotesRecord():
    def __init__(self):
        self.rec = votes_records

    def find(self, id):
        response = None
        for item in self.rec:
            if item['question_id'] == id:
                response = item
        return response

    def save(self, id, vote):
        ### True arguement is for an Upvote
        data = {
            "question_id" : id,
            "upvotes" : 0,
            "downvotes" : 0,
            "voted_on" : datetime.datetime.now()
        }
        ### True arguement is for an Upvote
        if vote:
            data['upvotes'] = data['upvotes'] + 1
            ### False arguement is for an downvote
        else:
            data['downvotes'] = data['downvotes'] + 1
        self.rec.append(data)
        return self.rec

    def upvote(self, id):
        record = self.find(id)
        if record is not None:  ### Record exists...
            record['upvotes'] = record['upvotes'] + 1
            return record
        else: ### record does not exists
            response = self.save(id, True)
        return response

    def downvote(self, id):
        record = self.find(id)
        if record is not None:  ### Record exists...
            record['downvotes'] = record['downvotes'] + 1
            return record
        else: ### record does not exists
            response = self.save(id, False)
        return response
