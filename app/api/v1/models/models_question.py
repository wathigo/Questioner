""" import the necessary modules """
import datetime
from .models_base import BaseModels


class QuestionRecord(BaseModels):
    """ Class to create a new meetup record """
    def __init__(self):
        self.record = BaseModels('question')

    def create_record(self, meetup_id, question):
        """ Create a meetup record """
        data = {
            "createdOn": datetime.datetime.now(),
            "id" : self.record.check_record_size() + 1,
            "meetupId" : meetup_id,
            "question" : question,
            "votes" : 0
        }
        self.record.save(data)
        return data

    def vote(self, question_id, vote):
        """ method to upvote/downvote a question """
        found = False
        item = self.record.find('id', question_id)
        if item:
            found = item[0]
            found_item = item
            if vote:
                found_item[0]['votes'] = found_item[0]['votes'] + 1
                found = found_item[0]
            elif found_item[0]['votes'] > 0:
                found_item[0]['votes'] = found_item[0]['votes'] - 1
                found = found_item[0]
        return found
