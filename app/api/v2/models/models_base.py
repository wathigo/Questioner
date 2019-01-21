""" Local imports """
from ....utils.database import db_conn


class BaseModels():
    """ Constructor that creates a connection and initilizes an instant variable table_name"""
    def __init__(self, record):
        self.connection = db_conn()
        self.table_name = record


    def check_exists(self, key, value):
        """ Check if an item exists in the database """
        record = self.check_record_type()
        items = [item for item in record if item[key] == value]
        return len(items)

    def find(self, key, value):
        """ Find an item with a specific key and value"""
        items = False
        record = self.check_record_type()
        item = [item for item in record if item[key] == value]
        if item:
            items = item
        return items

    def return_record(self):
        """ Return the whole data structure"""
        record = self.check_record_type()
        return record

    def save(self, query, data):
        """ Save data to a database"""
        save = self.connection
        cur = save.cursor()
        cur.execute(query)
        save.commit()
        return data

    def check_record_size(self):
        """ Check and return the size of the record """
        record = self.check_record_type()
        return len(record)

    def delete(self, key, value):
        """ Function to delete item """
        item = self.find(key, value)
        record = self.check_record_type()
        record.remove(item)
