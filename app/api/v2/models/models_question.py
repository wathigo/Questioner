"""Local imports """
from .models_base import BaseModels


class QuestionRecord(BaseModels):
    """ Class to create a new question record """
    def __init__(self):
        self.record = BaseModels('question')

    def create_record(self, meetup_id, question):
        """ Create a meetup record """
        data = {
            "meetupId" : meetup_id,
            "title" : question['title'],
            "question" : question['question'],
            "votes" : 0
        }
        query = """INSERT INTO question(meetupid, title, question, votes)
        VALUES ('%s', '%s', '%s', '%s')""" % \
        (data['meetupId'], data['title'], data['question'], data['votes'])
        self.record.save(query, data)
        return data

    def update_column_value(self, primary_key, value):
        """ Update votes column method """
        query = """ UPDATE question SET votes={} WHERE questionid={}""".format(value, primary_key)
        cur = self.record.connection.cursor()
        cur.execute(query)
        return self.record.find('questionid', primary_key)

    def vote(self, question_id, vote):
        ''' method to upvote/downvote a question '''
        data = False
        item = self.record.find('questionid', question_id)
        if item:
            found = item[3]
            if vote: ## Upvotes
                if found is None:
                    found = 0
                    found = found + 1
                    data = self.update_column_value(question_id, found)
                else:
                    found = found + 1
                    data = self.update_column_value(question_id, found)
            else:
                if found > 0 and found is not None:
                    found = found - 1
                    data = self.update_column_value(question_id, found)
                else:
                    data = self.record.find('questionid', question_id)
        return data
