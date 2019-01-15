""" import the necessary modules """
import json
from . import BaseTests


class TestUser(BaseTests):
    """ class to test users"""
    def create_record(self):
        """ Create a new user record for testing """
        response = self.client.post('/api/v1/auth/signup', \
            data=json.dumps({
                "FirstName": "David",
                "LastName": "Momanyi",
                "Email" : "momanyidavid@gmail.com",
                "Password" : "bill_Bond23",
                "RepeatPassword" : "bill_Bond23"
                }),\
            headers={"content-type": "application/json"})
        return response

    ###Test user account creation
    def test_01_post(self):
        """ Test user record creation"""
        response = self.create_record()
        self.assertEqual(response.status_code, 201)

    def test_02_post(self):
        """ Test for user login """
        self.create_record()
        response = self.client.post('/api/v1/auth/login', \
            data=json.dumps({
                "Email" : "momanyidavid@gmail.com",
                "Password" : "bill_Bond23",
                }),\
            headers={"content-type": "application/json"})
        self.assertEqual(response.status_code, 200)
