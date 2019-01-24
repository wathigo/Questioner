""" import the necessary modules"""
import re
import datetime
from marshmallow import ValidationError


class Views():
    """ Validate views endpoints data """
    def validate_email(self, email):
        """ Valiadte email format """
        response = False
        if re.match(r"(^[a-zA-z0-9_.]+@[a-zA-z0-9-]+\.[a-z]+$)", email) is None:
            raise ValidationError("Invalid email address!")
        return response

    def validate_password(self, password):
        """ Validate user password"""
        self.validate_all_values(password)
        if re.search('[0-9]', password) is None:
            raise ValidationError('Password must have at least one number!')

        elif re.search('[a-z]', password) is None:
            raise ValidationError('Password must have at least one alphabet letter!')

        else:
            return password

    def validate_all_values(self, value):
        """ Validate if all fields are provided """
        if isinstance(value, str):
            if not value.strip(' '):
                raise ValidationError('This field cannot be empty!')
        elif value:
            return value

    def validate_reserve(self, value):
        """ Validate reserve record"""
        self.validate_all_values(value)
        if value in('yes', 'no', 'maybe'):
            return value
        raise ValidationError("Wrong choice for this field. \
                               Valid choices are 'yes' 'no' or 'maybe'")

    def validate_date(self, value):
        """ Validate date object """
        if datetime.date.today() > value:
            raise ValidationError("Invalid date. Date passed is in the past.")
