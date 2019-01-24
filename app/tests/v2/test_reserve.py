""" import the necessary modules """
import json
from . import BaseTests


class TestReserve(BaseTests):
    """Tests for Reserve record requsts"""
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
        """ Create a new reserve record for testing"""
        admin = self.login_user()
        response = self.client.post('/api/v2/meetups/1/rsvps', \
            data=json.dumps({
                "status" : "yes"
                }),\
            headers={"Content-Type" : "application/json",
                     "Authorization" : "Bearer " + admin['access_token']})
        return response

    def test_01_post(self):
        """ Test post reserve endpoint"""
        response = self.create_record()
        self.assertEqual(response.status_code, 201)
