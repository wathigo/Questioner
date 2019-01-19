""" import the necessary modules """
from . import BaseTests
from ...utils.validators_schema import UserValidate

class TestValidators(BaseTests):
    """ class to test validators"""
    def test_user_registration(self):
        """ Validate user account creation """
        data = {
            "FirstName" : "",
            "LastName" : "Wathigo",
            "Email" : "wathigosimon@gmail.com",
            "Password" : "memory_Bad1",
            "RepeatPassword" :  "memory_Bad1"
            }
        data, errors = UserValidate().load(data)
        self.assertEqual(errors, {"FirstName": ["This field cannot be empty!"]})
        data['FirstName'] = 1
        data, errors = UserValidate().load(data)
        self.assertEqual(errors, {"FirstName": ["Not a valid string."]})
        data['Password'] = "memory_Bad"
        data, errors = UserValidate().load(data)
        self.assertEqual(errors, {"FirstName": ["Not a valid string."],\
                                      "Password": ["Password must have at least one number!"]})

#    def test_meetups_validation(self):
#        """ test cerate meetups data validation"""
    """    data = {
            "Title" : "Games",
            "Description" : "Chess playing",
            "Date" : "25th of december",
            "Loction" : "Kakamaga"
            }
        response = Views().validate_meetups(data)
        self.assertEqual(response, "Missing field!")""" """

    #def test_reserve_validation(self):"""
    """ Test for reserve validation"""
    """data = {
            "status" : ""
            }
        response = Views().validate_reserve_keys(data)
        self.assertEqual(response, "This field is required!")
        data['status'] = 1
        response = Views().validate_reserve_keys(data)
        self.assertEqual(response, "All fields must be strings!")"""
