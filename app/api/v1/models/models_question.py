import datetime
question_rec = []


class QuestionRecord():
    def __init__(self):
        self.rec = question_rec

    def save(self, question, id):
        data = {
            "createdOn": datetime.datetime.now(),
            "id" : len(question_rec) + 1,
            "meetupId" : id,
            "question" : question
        }
        self.rec.append(data)
        return self.rec
