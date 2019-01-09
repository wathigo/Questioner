""" import the necessary modules """

import unittest
import json

from app import create_app

from run import appl

class TestMeetups(unittest.TestCase):

    def setUp(self):
        appl.testing = True
        self.app = create_app()
        self.client = self.app.test_client()

    ###Test meetups creation
    def test_01_post(self):
        response = self.client.post('/api/v1/meetups', \
            data=json.dumps({
                "Title": "Gaming",
                "Description": "There will be a meetup for gamers on 25th of August..."
                }),\
            headers={"content-type": "application/json"})
        self.assertEqual(response.status_code, 200)
