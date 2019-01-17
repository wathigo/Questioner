import datetime
question_rec = []


class QuestionRecord():
    def __init__(self):
        self.rec = question_rec

    def save(self, meetup_id, question):
        data = {
            "createdOn": datetime.datetime.now(),
            "id" : len(question_rec) + 1,
            "meetupId" : meetup_id,
            "question" : question
        }
        self.rec.append(data)
        return self.rec
