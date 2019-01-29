""" import the necessary modules """
from . import BaseTests
from ...utils.validators_schema import UserValidate, MeetupValidate, QuestionValidate, ReserveValidate

class TestValidators(BaseTests):
    """ class to test validators"""
    def test_user_registration(self):
        """ Validate user account creation """
        record = {
            "firstname" : "",
            "lastname" : "Wathigo",
            "email" : "wathigosimon@gmail.com",
            "othername": "",
            "phonenumber" : "",
            "password" : "memory_Bad1",
            "repeatpassword" :  "memory_Bad1"
            }
        data, errors = UserValidate().load(record)
        self.assertEqual(errors, {"firstname": ["This field cannot be empty!"]})
        record['firstname'] = 1
        data, errors = UserValidate().load(record)
        self.assertEqual(errors, {"firstname": ["Not a valid string."]})
        record['password'] = "memory_Bad"
        data, errors = UserValidate().load(record)
        self.assertEqual(errors, {"firstname": ["Not a valid string."],\
                                      "password": ["Password must have at least one number!"]})

    def test_meetups_validation(self):
        """ test create meetups data validation"""
        record = {
            "title" : "Games",
            "description" : "Chess playing",
            "date" : "2020-05-19",
            "loction" : "Kakamaga"
            }
        data, errors = MeetupValidate().load(record)
        self.assertEqual(errors, {"location": ["Missing data for required field."]})

    def test_reserve_validation(self):
        """ Test for reserve validation"""
        data = {
            "status" : ""
            }
        data, errors = ReserveValidate().load(data)
        self.assertEqual(errors, {"status": ["This field cannot be empty!"]})
        data['status'] = 1
        data, errors = ReserveValidate().load(data)
        self.assertEqual(errors, {"status": ["Not a valid string."]})

    def test_question_validation(self):
        question_record = {
            "question" : 1
            }
        data, errors = QuestionValidate().load(question_record)
        self.assertEqual(errors, {"question": ["Not a valid string."]})
        BaseTests().tearDown()
