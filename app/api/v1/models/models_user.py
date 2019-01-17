""" import database module """
from ....utils.database import db_conn, create_tables


class UserRecord():
    """ Views for user records """
    def __init__(self):
        self.db = db_conn()

    def save(self, fname, lname, email, password):
        """ Add a new record entry to the data structure"""
        data = {
            "FirstName" : fname,
            "LastName" : lname,
            "Email" : email,
            "Password" : password
        }
        query = """INSERT INTO users(FirstName, LastName, Email, Password)
        VALUES ('%s', '%s', '%s', '%s');""" % \
        (data['FirstName'], data['LastName'], data['Email'], data['Password'])

        save = self.db
        cur = save.cursor()
        cur.execute(query)
        save.commit()
        return data


"""    def authenticate_user(self, email, password):
         Check if user exists and compare password
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
        return login  """
