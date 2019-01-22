"""Local imports """
from .models_base import BaseModels


class QuestionRecord(BaseModels):
    """ Class to create a new question record """
    def __init__(self):
        self.record = BaseModels('question')

    def create_record(self, meetup_id, question, email):
        """ Create a meetup record """
        meetup_record = BaseModels('meetups')
        meetup = meetup_record.find('meetupid', meetup_id)# check if the meetup exists
        if not meetup:
            return False # Return false if it does not exist
        user_record = BaseModels('user_table') ## Check the userid from the user_table using the
        user = user_record.find('email', email) # email obtained from the jwt object identity
        userid = user[0]

        data = {
            "meetupId" : meetup_id,
            "userid" : userid,
            "title" : question['title'],
            "question" : question['question'],
            "votes" : 0
        }
        query = """INSERT INTO question(meetupid, title, question, votes)
        VALUES ('%s', '%s', '%s', '%s')""" % \
        (data['meetupId'], data['title'], data['question'], data['votes'])
        self.record.save(query, data)
        return data

    def update_column_value(self, primary_key, vote):
        """ Update votes column method """
        if vote:
            query = """ UPDATE question SET votes=votes+1 WHERE questionid={}""".format(primary_key)
        else:
            query = """ UPDATE question SET votes=votes-1 WHERE questionid={}""".format(primary_key)
        cur = self.record.connection.cursor()
        cur.execute(query)
        return self.record.find('questionid', primary_key)

    def modify_response(self, data):
        """ Method to modify question record response(turple->dict) """
        response = {
            "Title" : data[1],
            "Question" : data[2],
            "Votes" : data[3]
            }
        return response

    def vote(self, question_id, vote):
        ''' method to upvote/downvote a question '''
        data = False
        item = self.record.find('questionid', question_id)
        if item:
            if not vote and item[3] < 1:
                data = self.modify_response(item)
            else:
                record = self.update_column_value(question_id, vote)
                data = self.modify_response(record)
        return data
