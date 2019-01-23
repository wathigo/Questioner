""" import models_base module """
from .models_base import BaseModels


class UserRecord():
    """ Views for user records """
    def __init__(self):
        self.models = BaseModels('user_table')

    def create_user(self, user_data, role):
        ''' Add a new record entry to the data structure'''
        exists = self.models.check_exists('email', user_data['Email'])
        if exists is not None:
            return None
        data = {
            "isadmin" : False,
            "FirstName" : user_data['FirstName'],
            "LastName" : user_data['LastName'],
            "OtherName" : user_data['OtherName'],
            "UserName" : user_data['Email'].split("@")[0],
            "PhoneNumber" : user_data['PhoneNumber'],
            "Email" : user_data['Email'],
            "Password" : user_data['Password']
        }
        if role: # if admin
            data['isadmin'] = True
        query = """INSERT INTO user_table(isadmin, firstname, lastname, username, \
                                          othername, phonenumber, email, password)
        VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s');""" % \
        (data['isadmin'], data['FirstName'], data['LastName'],\
         data['UserName'], data['OtherName'],\
         data['PhoneNumber'], data['Email'], data['Password'])
        data = self.models.save(query, data)
        return data

    def authenticate_user(self, data):
        ''' Check if a user exists and compare passwords'''
        result = True
        found = self.models.check_exists('email', data['Email'])
        if not found:
            return None
        credentials = self.models.find('email', data['Email'])
        if credentials['password'] != data['Password']:
            result = False
        return result
