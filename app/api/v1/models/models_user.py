""" import datetime module """
import datetime
USER_RECORDS = []


class UserRecord():
    """ Views for user records """
    def __init__(self):
        self.records = USER_RECORDS

    def save(self, fname, lname, email, password):
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
