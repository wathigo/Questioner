""" import the necessary modules """
import json
from . import BaseTests


class TestVotes(BaseTests):
    """ class to test votes endpoints """
    def test_patch_upvote(self):
        """ test upvote endpoint"""
        response = self.client.patch('/api/v2/questions/1/upvote', \
            headers={"content-type": "application/json"})
        self.assertEqual(response.status_code, 201)

    def test_patch_downvote(self):
        """ Test downvote endpoint"""
        response = self.client.patch('/api/v2/questions/1/downvote', \
            headers={"content-type": "application/json"})
        self.assertEqual(response.status_code, 201)
