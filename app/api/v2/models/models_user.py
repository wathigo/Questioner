""" import models_base module """
from .models_base import BaseModels


class UserRecord():
    """ Views for user records """
    def __init__(self):
        self.models = BaseModels('user_table')

    def create_user(self, user_data, role):
        ''' Add a new record entry to the database'''
        if user_data['password'] != user_data['repeatpassword']:
            return 'f'
        exists = self.models.check_exists('email', user_data['email'])
        found = exists
        print(found)
        if found['exists']:
            return False
        data = {
            "isadmin" : False,
            "FirstName" : user_data['firstname'],
            "LastName" : user_data['lastname'],
            "OtherName" : user_data['othername'],
            "UserName" : user_data['email'].split("@")[0],
            "PhoneNumber" : user_data['phonenumber'],
            "Email" : user_data['email'],
            "Password" : user_data['password']
        }
        if role: # if admin
            data['isadmin'] = True
        query = """INSERT INTO user_table(isadmin, firstname, lastname, username, \
                                          othername, phonenumber, email, password)
        VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s');""" % \
        (data['isadmin'], data['FirstName'], data['LastName'],\
         data['UserName'], data['OtherName'],\
         data['PhoneNumber'], data['Email'], data['Password'])
        response = self.models.save(query, data)
        return response

    def authenticate_user(self, data):
        ''' Check if a user exists and compare passwords'''
        result = True
        credentials = self.models.find('email', data['Email'])
        if credentials is None:
            result = 'f'
        if credentials['password'] != data['Password']:
            result = False
        return result
