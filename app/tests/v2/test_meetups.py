""" import the necessary modules """
import json
from .test_users import TestUser
from . import BaseTests

class TestMeetups(BaseTests):
    """ Class to test meetup record requests """
    def login_user(self):
        """ Create a new user record for testing """
        response = self.client.post('/api/v2/auth/login', \
         data=json.dumps({
             "email" : "wathigosimon@gmail.com",
             "password" : "memory_Bad1"
             }),\
         headers={"content-type": "application/json"})
        response_data = response.json
        return response_data
    def create_record(self):
        """ craete a new meetup record for testing"""
        admin = self.login_user()
        token = admin['access_token']
        response = self.client.post('/api/v2/meetups', \
            data=json.dumps({
                "title": "Gaming",
                "description": "There will be a meetup for gamers on 25th of August...",
                "date" : "2020-09-23",
                "location" : "Moi Avenue"
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

    def test_04_delete(self):
        """ Test for delete meetup endpont"""
        response, token = self.create_record()
        response = self.client.delete('/api/v2/meetups/1', \
        headers={"Content-Type" : "application/json",
                 "Authorization" : "Bearer " + token})
        self.assertEqual(response.status_code, 200)
