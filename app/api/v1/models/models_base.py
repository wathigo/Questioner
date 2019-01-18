""" Create data structures for the models """
MEETUP_RECORD = []
QUESTION_RECORD = []
USER_RECORD = []


class BaseModels(object):
    """ Constructer instantiation record variable with the record type"""
    def __init__(self, record):
        self.record = record

    def check_record_type(self):
        """ Check the record type and return a reference to the data structure"""
        if self.record == 'meetup':
            record_type = MEETUP_RECORD
        elif self.record == 'question':
            record_type = QUESTION_RECORD
        elif self.record == 'user':
            record_type = USER_RECORD
        return record_type

    def check_exists(self, key, value):
        """ Check if an item exists in the data structure """
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

    def save(self, data):
        """ Save data to a database"""
        record = self.check_record_type()
        record.append(data)
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
