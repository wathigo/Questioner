""" import the necessary modules """
import json
from . import BaseTests

class TestMeetups(BaseTests):
    """ Class to test meetup record requests """
    def create_record(self):
        """ craete a new meetup record for testing"""
        response = self.client.post('/api/v1/meetups', \
            data=json.dumps({
                "Title": "Gaming",
                "Description": "There will be a meetup for gamers on 25th of August...",
                "Date" : "25th of November",
                "Location" : "Moi Avenue"
                }),\
            headers={"content-type": "application/json"})
        return response

    ###Test meetups creation
    def test_01_post(self):
        """ test meetup creation endpoint"""
        response = self.create_record()
        self.assertEqual(response.status_code, 201)

    def test_02_get(self):
        """ Test get all meetup records endpoint"""
        response = self.client.get('/api/v1/meetups/upcoming', \
        headers={"content-type": "application/json"})
        self.assertEqual(response.status_code, 200)

    def test_03_get(self):
        """ Test get specific meetup endpoint"""
        self.create_record()
        response = self.client.get('/api/v1/meetups/1', \
        headers={"content-type": "application/json"})
        self.assertEqual(response.status_code, 200)

    def test_o4_put(self):
        """ Test put meetup endpoint"""
        self.create_record()
        response = self.client.put('/api/v1/meetups/1', \
            data=json.dumps({
                "Title": "Gaming",
                "Description": "There will be a meetup for gamers on 25th of August...",
                "Date" : "25th of August",
                "Location" : "Andela Kenya"
                }), headers={"content-type": "application/json"})
        self.assertEqual(response.status_code, 200)
