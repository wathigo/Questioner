""" import the necessary modules """
import json
from . import BaseTests

class TestQuestions(BaseTests):
    """ class to test question endpoint """
    def create_record(self):
        """ Craete a record for testing"""
        response = self.client.post('/api/v2/meetups/1/questions', \
            data=json.dumps({
                "question" : "What are the basic moves in hip hop?"
                }),\
            headers={"content-type": "application/json"})
        return response

    def test_01_post(self):
        """ Test to test for post question endpoint"""
        response = self.create_record()
        self.assertEqual(response.status_code, 201)
