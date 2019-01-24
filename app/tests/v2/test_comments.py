""" import the necessary modules """
import json
from . import BaseTests

class TestComments(BaseTests):
    """ Class to test meetup record requests """
    def create_user_record(self):
        """ Create a new user record for testing """
        response = self.client.post('/api/v2/auth/admin/signup', \
         data=json.dumps({
             "FirstName": "David",
             "LastName": "Momanyi",
             "Email" : "momanyidavid@gmail.com",
             "OtherName" : "",
             "PhoneNumber" : "",
             "Password" : "bill_Bond23",
             "RepeatPassword" : "bill_Bond23"
             }),\
         headers={"content-type": "application/json"})
        response_data = response.json
        return response_data

    def create_record(self):
        """ craete a new comment record for testing"""
        admin = self.create_user_record()
        token = admin['access_token']
        response = self.client.post('/api/v2/question/1/comments', \
            data=json.dumps({
                "comment" : "sounds great!"
                }),\
            headers={"Content-Type" : "application/json",
                     "Authorization" : "Bearer " + token})
        return response, token
