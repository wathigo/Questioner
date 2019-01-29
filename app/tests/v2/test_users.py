""" import the necessary modules """
import json
from . import BaseTests


TOKEN = None
class TestUser(BaseTests):
    """ class to test users"""
    def create_record(self):
        """ Create a new user record for testing """
        response = self.client.post('/api/v2/auth/admin/signup', \
            data=json.dumps({
                "firstname": "David",
                "lastname": "Momanyi",
                "email" : "kamaudav@gmail.com",
                "othername" : "",
                "phonenumber" : "",
                "password" : "bill_Bond23",
                "repeatpassword" : "bill_Bond23"
                }),\
            headers={"content-type": "application/json"})
        response_data = response.json
        return response_data

    ###Test user account creation
    def test_01_post(self):
        """ Test user record creation"""
        response = self.create_record()
        self.assertEqual(response['status'], 201)

    def test_02_post(self):
        """Test for user login"""
        data = self.create_record()
        response = self.client.post('/api/v2/auth/login', \
            data=json.dumps({
                "email" : "kamaudav@gmail.com",
                "password" : "bill_Bond23",
                }),\
            headers={"content-type": "application/json"})
        self.assertEqual(response.status, '200 OK')
