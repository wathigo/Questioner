""" import the necessary modules"""
import re


class Views():
    """ Validate views """
    def validate_user(self, data):
        """ validate user registration"""
        response = False
        response = self.validate_all_values(data)
        response = self.validate_string(data)
        try:
            fname = data['FirstName']
            lname = data['LastName']
            email = data['Email']
            password = data['Password']
            rpassword = data['RepeatPassword']
        except KeyError:
            response = "Missing field!"
        valid_email = self.validate_email(email)
        valid_password = self.validate_password(password)
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
            response = 'Missing field!'
        response = self.validate_string(data)
        valid_email = self.validate_email(email)
        valid_password = self.validate_password(password)
        if valid_email:
            response = valid_email
        if valid_password:
            response = valid_password
        response = self.validate_all_values(data)
        return response

    def validate_email(self, email):
        """ Valiadte email format """
        response = False
        if re.match(r"(^[a-zA-z0-9_.]+@[a-zA-z0-9-]+\.[a-z]+$)", email) is None:
            response = "Invalid email address!"
        return response

    def validate_password(self, password):
        """ Validate user password"""
        if re.search('[0-9]', password) is None:
            response = 'Password must have at least one number!'

        elif re.search('[a-z]', password) is None:
            response = 'Password must have at least one alphabet letter!'

        else:
            return False
        return response


    def validate_meetups(self, data):
        """ Validate meetups requests"""
        response = False
        try:
            title = data['Title']
            description = data['Description']
            date = data['Date']
            location = data['Location']
        except KeyError:
            response = "Missing field!"
        invalid_data = self.validate_all_values(data)
        if invalid_data:
            response = invalid_data
        return response


    def validate_question_keys(self, data):
        """ Edge case for post question request endpoint"""
        response = False
        try:
            question = data['question']

        except KeyError:
            response = "Missing field!"
        invalid = self.validate_all_values(data)
        if invalid:
            response = "This value for this field is required!"
        return response

    def validate_reserve_keys(self, data):
        """ Edge case for post reserve request """
        response = False
        try:
            status = data['status']

        except KeyError:
            response = "Missing fied!"
        invalid_value = self.validate_all_values(data)
        is_string = self.validate_string(data)
        if is_string:
            response = is_string
        if invalid_value:
            response = "This field is required!"
        return response

    def validate_all_values(self, data):
        """ Validate if all fields are provided """
        response = False
        for key in data:
            if data[key] == "":
                response = "All values for the fields are required!"
        return response

    def validate_string(self, data):
        """ Valiadate if a value is a string"""
        response = False
        if isinstance(data, dict):
            for key in data:
                if not isinstance(data[key], str):
                    response = "All fields must be strings!"
        elif not isinstance(data, str):
            response = "This field must be a string!"
        return response
