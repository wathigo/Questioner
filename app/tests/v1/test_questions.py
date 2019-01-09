""" import the necessary modules """

import unittest
import json

from app import create_app

from run import appl

""" class to test question endpoint """
class TestQuestions(unittest.TestCase):

    def setUp(self):
        appl.testing = True
        self.app = create_app()
        self.client = self.app.test_client()

    def create_record(self):
        response = self.client.post('/api/v1/meetups/1/questions', \
            data=json.dumps({
                "question" : "What are the basic moves in hip hop?"
                }),\
            headers={"content-type": "application/json"})
        return response

    def test_01_post(self):
        response = self.create_record()
        self.assertEqual(response.status_code, 201)
