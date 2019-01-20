""" import third party modules """
from marshmallow import Schema, fields
from .validators import Views


class UserValidate(Schema):
    """ Validate data for user registration """
    FirstName = fields.Str(required=True, validate=Views().validate_all_values)
    LastName = fields.Str(required=True, validate=Views().validate_all_values)
    Email = fields.Str(required=True, validate=Views().validate_all_values)
    Password = fields.Str(required=True, validate=Views().validate_password)


class MeetupValidate(Schema):
    """ Validate data for meetup creation """
    Title = fields.Str(required=True, validate=Views().validate_all_values)
    Description = fields.Str(required=True, validate=Views().validate_all_values)
    Date = fields.Date(required=True)
    Location = fields.Str(required=True, validate=Views().validate_all_values)


class QuestionValidate(Schema):
    """ Validate data for question creation """
    question = fields.Str(required=True, validate=Views().validate_all_values)


class ReserveValidate(Schema):
    """ Validate data for meetup reserve endpoint """
    status = fields.Str(required=True, validate=Views().validate_reserve)
