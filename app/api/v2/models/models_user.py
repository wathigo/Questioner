""" import models_base module """
from .models_base import BaseModels


class UserRecord():
    """ Views for user records """
    def __init__(self):
        self.models = BaseModels('user_table')

    def create_user(self, user_data):
        """ Add a new record entry to the data structure"""
        data = {
            "FirstName" : user_data['FirstName'],
            "LastName" : user_data['LastName'],
            "OtherName" : user_data['OtherName'],
            "UserName" : user_data['Email'].split("@")[0],
            "PhoneNumber" : user_data['PhoneNumber'],
            "Email" : user_data['Email'],
            "Password" : user_data['Password']
        }
        query = """INSERT INTO user_table(firstname, lastname, username, \
                                          othername, phonenumber, email, password)
        VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s');""" % \
        (data['FirstName'], data['LastName'], data['OtherName'], data['UserName'],\
         data['PhoneNumber'], data['Email'], data['Password'])
        data = self.models.save(query, data)
        return data

    def authenticate_user(self, data):
        
