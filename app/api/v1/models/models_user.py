""" import datetime module """
import datetime
from .models_base import BaseModels


class UserRecord(BaseModels):
    """ Models for user records """
    def __init__(self):
        self.user_records = BaseModels('user')

    def create_user(self, fname, lname, email, password):
        """ Add a new record entry to the data structure"""
        data = {
            "userId" : self.user_records.check_record_size()+1,
            "CreatedOn" : datetime.datetime.now(),
            "FirstName" : fname,
            "LastName" : lname,
            "Email" : email,
            "Password" : password
        }
        self.user_records.save(data)
        return data

    def authenticate_user(self, email, password):
        """ Check if user exists and compare password"""
        user_record = self.user_records.find('Email', email)
        login = False
        if user_record:
            user = user_record
            if user[0]['Password'] == password:
                login = "Login successful"
            else:
                login = 'f'
        return login
