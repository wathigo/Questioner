""" import the necessary modules """
import json
from .test_users import TestUser
from . import BaseTests

class TestMeetups(BaseTests):
    """ Class to test meetup record requests """
    def create_admin_record(self):
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
        """ craete a new meetup record for testing"""
        admin = self.create_admin_record()
        token = admin['access_token']
        response = self.client.post('/api/v2/meetups', \
            data=json.dumps({
                "Title": "Gaming",
                "Description": "There will be a meetup for gamers on 25th of August...",
                "Date" : "1971-09-23",
                "Location" : "Moi Avenue"
                }),\
            headers={"Content-Type" : "application/json",
                     "Authorization" : "Bearer " + token})
        return response, token

    ###Test meetups creation
    def test_01_post(self):
        """ test meetup creation endpoint"""
        response, token = self.create_record()
        self.assertEqual(response.status_code, 201)

    def test_02_get(self):
        """ Test get all meetup records endpoint"""
        response, token = self.create_record()
        response = self.client.get('/api/v2/meetups/upcoming', \
        headers={"Content-Type" : "application/json",
                 "Authorization" : "Bearer " + token})
        self.assertEqual(response.status_code, 200)

    def test_03_get(self):
        """ Test get specific meetup endpoint"""
        response, token = self.create_record()
        response = self.client.get('/api/v2/meetups/1', \
        headers={"Content-Type" : "application/json",
                 "Authorization" : "Bearer " + token})
        self.assertEqual(response.status_code, 200)

    def test_o4_put(self):
        """ Test put meetup endpoint"""
        admin = self.create_admin_record()
        self.create_record()
        response = self.client.put('/api/v2/meetups/1', \
            data=json.dumps({
                "Title": "Gaming",
                "Description": "There will be a meetup for gamers on 25th of August...",
                "Date" : "2019-09-23",
                "Location" : "Andela Kenya"
                }), headers={"Content-Type" : "application/json",
                             "Authorization" : "Bearer " + admin['access_token']})
        self.assertEqual(response.status_code, 200)
