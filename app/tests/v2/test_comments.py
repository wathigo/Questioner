""" import the necessary modules """
import json
from . import BaseTests

class TestComments(BaseTests):
    """ Class to test meetup record requests """
    def login_user(self):
        """ Create a new user record for testing """
        response = self.client.post('/api/v2/auth/login', \
         data=json.dumps({
             "Email" : "wathigosimon@gmail.com",
             "Password" : "memory_Bad1"
             }),\
         headers={"content-type": "application/json"})
        response_data = response.json
        return response_data

    def create_record(self):
        """ craete a new comment record for testing"""
        admin = self.login_user()
        token = admin['access_token']
        response = self.client.post('/api/v2/question/2/comments', \
            data=json.dumps({
                "comment" : "sounds great!"
                }),\
            headers={"Content-Type" : "application/json",
                     "Authorization" : "Bearer " + token})
        return response

    def test_01_post(self):
        data = self.create_record()
        self.assertEqual(data.status_code, 404)
