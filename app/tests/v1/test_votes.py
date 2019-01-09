""" import the necessary modules """

import unittest
import json
from app import create_app
from run import appl


""" class to test votes endpoints """
class TestVotes(unittest.TestCase):

    def setUp(self):
        appl.testing = True
        self.app = create_app()
        self.client = self.app.test_client()

    def test_patch_upvote(self):
        response = self.client.patch('/api/v1/questions/1/upvote', \
            headers={"content-type": "application/json"})
        self.assertEqual(response.status_code, 201)

    def test_patch_downvote(self):
        response = self.client.patch('/api/v1/questions/1/downvote', \
            headers={"content-type": "application/json"})
        self.assertEqual(response.status_code, 201)
