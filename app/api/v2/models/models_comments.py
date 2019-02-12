""" local imports """
from .models_base import BaseModels

class CommentsRecord():
    """ class to define methods utilized by comment views"""
    def __init__(self):
        self.record = BaseModels('comments')

    def create_comment_record(self, data, questionid, email):
        """ method to create a comment record"""
        user = BaseModels('user_table')
        user_data = user.find('email', email)
        userid = user_data['userid']
        question = BaseModels('question')
        question_data = question.find('questionid', questionid)
        question_title = question_data['title']
        question_body = question_data['question']
        comment = data['comment']
        data = {
            "questionid" : questionid,
            "userid" : userid,
            "body" : question_body,
            "title" : question_title,
            "comment" : comment
        }
        query = """INSERT INTO comments(questionid, userid, body, title)
        VALUES ('%s', '%s', '%s', '%s') RETURNING userid, questionid, title, body, comment""" % \
        (data['questionid'], data['userid'], data['body'], data['title'])
        response = self.record.save(query)
        return response
