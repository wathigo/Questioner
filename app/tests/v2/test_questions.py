""" import the necessary modules """
import json
from . import BaseTests

class TestQuestions(BaseTests):
    """ class to test question endpoint """
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
        user = self.login_user()
        response = self.client.post('/api/v2/meetups/1/questions', \
            data=json.dumps({
                "title" : "Dancing",
                "question" : "What are the moves in hip hop?"
                }),\
            headers={"Content-Type" : "application/json",
                     "Authorization" : "Bearer " + user['access_token']})
        return response

    def test_01_post(self):
        response = self.create_record()
        print(response)
        self.assertEqual(response.status_code, 201)
