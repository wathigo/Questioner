""" import the necessary modules """

import unittest
import json
from app import create_app
from run import appl


""" class to test reserve endpoint """
class TestQuestions(unittest.TestCase):

    def setUp(self):
        appl.testing = True
        self.app = create_app()
        self.client = self.app.test_client()

    def create_record(self):
        response = self.client.post('/api/v1/meetups/1/rsvps', \
            data=json.dumps({
                "status" : "yes"
                }),\
            headers={"content-type": "application/json"})
        return response

    def test_01_post(self):
        response = self.create_record()
        self.assertEqual(response.status_code, 201)
