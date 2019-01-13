""" import the necessary modules"""
import re


class Views():
    """ Validate views """
    def validate_user(self, data):
        """ validate user registration"""
        response = False
        try:
            fname = data['FirstName']
            lname = data['LastName']
            email = data['Email']
            password = data['Password']
            rpassword = data['RepeatPassword']
        except KeyError:
            response = "Invalid keys"
        valid_email = self.validate_email(email)
        valid_password = self.validate_password(password)
        for key in data:
            if not data[key]:
                response = 'All fields are required'
        if password != rpassword:
            response = "password does not match!"
        if valid_password is not False:
            response = valid_password
        if valid_email is not False:
            response = valid_email
        return response

    def validate_user_login(self, data):
        """ Validate user login """
        response = False
        try:
            email = data['Email']
            password = data['Password']
        except KeyError:
            response = 'Invalid keys'
        valid_email = self.validate_email(email)
        valid_password = self.validate_password(password)
        if valid_email:
            response = valid_email
        if valid_password:
            response = valid_password
        return response

    def validate_email(self, email):
        response = False
        if re.match(r"(^[a-zA-z0-9_.]+@[a-zA-z0-9-]+\.[a-z]+$)", email) is None:
            response = "Invalid email address!"
        return response

    def validate_password(self, password):
        if len(password) < 9:
            response = "Password must be at least 8 characters long!"

        elif re.search('[0-9]', password) is None:
            response = 'Password must have at least one number!'

        elif re.search('[A-Z]', password) is None:
            response = 'Password must have at least one capital letter!'

        elif re.search('[a-z]', password) is None:
            response = 'Password must have at least one alphabet letter!'

        elif re.search('[!,#,$,%,&,*,+,-,<,=,>,?,@,^,_,{,|,},~,]', password) is None:
            response = 'Password must have at least a special character!'

        else:
            return False
        return response


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
