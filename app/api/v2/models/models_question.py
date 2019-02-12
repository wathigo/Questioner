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
        userid = user['userid']
        title = self.record.find('title', question['title'])
        question_data = self.record.find('question', question['question'])
        if title and question_data:
            return 'f'

        data = {
            "meetupId" : meetup_id,
            "userid" : userid,
            "title" : question['title'],
            "question" : question['question'],
            "votes" : 0
        }
        query = """INSERT INTO question(meetupid, userid, title, question, votes)
        VALUES ('%s', '%s', '%s', '%s', '%s') \
        RETURNING questionid, title, meetupid, userid, question, votes, askedon""" % \
        (data['meetupId'], data['userid'], data['title'], data['question'], data['votes'])
        response = self.record.save(query, data)
        print(response)
        return response

    def update_column_value(self, primary_key, vote):
        """ Update votes column method """
        if vote:
            query = """ UPDATE question SET votes=votes+1 WHERE questionid={}\
                        RETURNING json_build_object('meetupid', meetupid, 'userid', userid, 'title', \
                                    title, 'question', question, 'votes', votes)""".format(primary_key)
        else:
            question_record = self.record.find('questionid', primary_key)
            if question_record['votes'] > 0:
                query = """ UPDATE question SET votes=votes-1 WHERE questionid={}\
                    RETURNING json_build_object('meetupid', meetupid, 'userid', userid, 'title', \
                                title, 'question', question, 'votes', votes)""".format(primary_key)
            else:
                return question_record
        response = self.record.return_record(query)
        self.record.connection.close()
        return response

    def vote(self, question_id, vote):
        ''' method to upvote/downvote a question '''
        record = self.update_column_value(question_id, vote)
        return record
