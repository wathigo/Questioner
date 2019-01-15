""" import the necessary modules """
from . import BaseTests
from ...utils.validators import Views

class TestValidators(BaseTests):
    """ class to test validators"""
    def test_user_registration(self):
        """ Validate user account creation """
        data = {
            "FirstName" : "Simon",
            "LastName" : "Wathigo",
            "Email" : "wathigosimongmail.com",
            "Password" : "memory_Bad1",
            "RepeatPassword" :  "memory_Bad1"
            }
        response = Views().validate_user(data)
        self.assertEqual(response, "Invalid email address!")
        data['FirstName'] = 1
        data['Email'] = "wathigosimon@gmail.com"
        response = Views().validate_user(data)
        self.assertEqual(response, "All fields must be strings!")

    def test_user_login(self):
        """ Test for user login validators"""
        data = {
            "Email" : "wathigosimon@gmail.com",
            "Password" : ""
            }
        response = Views().validate_user_login(data)
        self.assertEqual(response, "All fields are required!")

    def test_meetups_validation(self):
        """ test cerate meetups data validation"""
        data = {
            "Title" : "Games",
            "Description" : "Chess playing",
            "Date" : "25th of december",
            "Loction" : "Kakamaga"
            }
        response = Views().validate_meetups(data)
        self.assertEqual(response, "invalid key!")

    def test_reserve_validation(self):
        """ Test for reserve validation"""
        data = {
            "status" : ""
            }
        response = Views().validate_reserve_keys(data)
        self.assertEqual(response, "This field is required!")
        data['status'] = 1
        response = Views().validate_reserve_keys(data)
        self.assertEqual(response, "All fields must be strings!")
