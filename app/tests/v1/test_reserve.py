""" import the necessary modules """
import json
from . import BaseTests


class TestReserve(BaseTests):
    """Tests for Reserve record requsts"""
    def create_record(self):
        """ Create a new reserve record for testing"""
        response = self.client.post('/api/v1/meetups/1/rsvps/user/1', \
            data=json.dumps({
                "status" : "yes"
                }),\
            headers={"content-type": "application/json"})
        return response

    def test_01_post(self):
        """ Test post reserve endpoint"""
        response = self.create_record()
        self.assertEqual(response.status_code, 201)
