""" import third party modules """
from marshmallow import Schema, fields
from .validators import Views


class UserValidate(Schema):
    """ Validate data for user registration """
    FirstName = fields.Str(required=True, validate=Views().validate_all_values)
    LastName = fields.Str(required=True, validate=Views().validate_all_values)
    Email = fields.Str(required=True, validate=Views().validate_all_values)
    Password = fields.Str(required=True, validate=Views().validate_password)
    RepeatPassword = fields.Str(required=True)
    OtherName = fields.Str(required=True)
    PhoneNumber = fields.Str(required=True)


class MeetupValidate(Schema):
    """ Validate data for meetup creation """
    Title = fields.Str(required=True, validate=Views().validate_all_values)
    Description = fields.Str(required=True, validate=Views().validate_all_values)
    Date = fields.Date(required=True, validate=Views().validate_date)
    Location = fields.Str(required=True, validate=Views().validate_all_values)


class QuestionValidate(Schema):
    """ Validate data for question creation """
    question = fields.Str(required=True, validate=Views().validate_all_values)


class ReserveValidate(Schema):
    """ Validate data for meetup reserve endpoint """
    status = fields.Str(required=True, validate=Views().validate_reserve)
