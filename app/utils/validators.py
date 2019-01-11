
""" Class to validate views """
class Views():
    """ Edge cases for views """
    def validate_keys(self, data):
        try:
            title = data['Title']
            description = data['Description']
            date = data['Date']
            location = data['Location']

        except KeyError:
            data = False
        return data

    def validate_question_keys(self, data):
        """ Edge case for post question request endpoint"""
        try:
            question = data['question']

        except KeyError:
            data = False
        return data

    def validate_reserve_keys(self, data):
        """ Edge case for post reserve request """
        try:
            status = data['status']

        except KeyError:
            data = False
        return data
