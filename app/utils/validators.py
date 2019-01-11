
""" Class to validate views """
class Views():
    """ Validate post meetup request keys """
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
        try:
            question = data['question']

        except:
            data = False
        return data
