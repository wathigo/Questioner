""" Local imports """
from ....utils.database import db_conn


class BaseModels():
    ''' Constructor that creates a connection and initilizes an instant variable table_name'''
    def __init__(self, record):
        self.connection = db_conn()
        self.table_name = record


    def check_exists(self, key, value):
        ''' Check if an item exists in the database '''
        query = """ SELECT EXISTS (SELECT * FROM {} WHERE {}='{}');""" \
                    .format(self.table_name, key, value)
        cur = self.connection.cursor()
        cur.execute(query)
        found = cur.fetchone()
        return found[0]

    def find(self, key, value):
        ''' Find an item with a specific key and value'''
        query = """ SELECT * FROM {} WHERE {}='{}'""".format(self.table_name, key, value)
        cur = self.connection.cursor()
        cur.execute(query)
        data = cur.fetchone()
        return data

    def return_record(self):
        ''' Return the whole database'''
        query = """ SELECT * FROM {}""".format(self.table_name)
        cur = self.connection.cursor()
        cur.execute(query)
        data = cur.fetchall()
        return data

    def save(self, query, data):
        ''' Save data to a database'''
        save = self.connection
        cur = save.cursor()
        cur.execute(query)
        save.commit()
        return data


    def delete(self, key, value):
        '''Function to delete of an a row item'''
        data = self.check_exists(key, value)
        if data:
            query = """ DELETE FROM {} WHERE {}='{}'""".format(self.table_name, key, value)
            cur = self.connection.cursor()
            cur.execute(query)
