""" import datetime module """
import datetime
USER_RECORDS = []


class UserRecord():
    """ Views for user records """
    def __init__(self):
        self.records = USER_RECORDS

    def save(self, fname, lname, email, password):
        """ Add a new record entry to the data structure"""
        data = {
            "userId" : len(self.records)+1,
            "CreatedOn" : datetime.datetime.now(),
            "FirstName" : fname,
            "LastName" : lname,
            "Email" : email,
            "Password" : password
        }
        self.records.append(data)
        return self.records

    def authenticate_user(self, email, password):
        """ Check if user exists and compare password"""
        user = None
        login = False
        for item in self.records:
            if item['Email'] == email:
                user = item
                break
        if user is not None:
            if user['Password'] == password:
                login = 'Login successful'
            else:
                login = 'f'
        return login
