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
            "firstname" : user_data['firstname'],
            "lastname" : user_data['lastname'],
            "othername" : user_data['othername'],
            "username" : user_data['email'].split("@")[0],
            "phonenumber" : user_data['phonenumber'],
            "email" : user_data['email'],
            "password" : user_data['password']
        }
        if role: # if admin
            data['isadmin'] = True
        query = """INSERT INTO user_table(isadmin, firstname, lastname, username, \
                                          othername, phonenumber, email, password)
        VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s') RETURNING userid, isadmin, firstname, lastname, email;""" % \
        (data['isadmin'], data['firstname'], data['lastname'],\
         data['username'], data['othername'],\
         data['phonenumber'], data['email'], data['password'])
        response = self.models.save(query)
        return response

    def authenticate_user(self, data):
        ''' Check if a user exists and compare passwords'''
        result = True
        credentials = self.models.find('email', data['email'])
        if credentials is None:
            result = 'f'
        elif credentials['isadmin'] == True:
            result = 'isadmin'
        if credentials['password'] != data['password']:
            result = False
        print (result)
        return result
