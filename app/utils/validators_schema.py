""" import third party modules """
from marshmallow import Schema, fields
from .validators import Views


class UserValidate(Schema):
    """ Validate data for user registration """
    FirstName = fields.Str(required=True, validate=Views().validate_all_values)
    LastName = fields.Str(required=True, validate=Views().validate_all_values)
    Email = fields.Str(required=True, validate=Views().validate_all_values)
    Password = fields.Str(required=True, validate=Views().validate_password)
    RepeatPassword = fields.Str(required=True, validate=Views().validate_password)

class MeetupValidate(Schema):
    """ Validate data for mee creation """
    Title = fields.Str(required=True, validate=Views().validate_all_values)
    Description = fields.Str(required=True, validate=Views().validate_all_values)
    Date = fields.Date(required=True)
    Location = fields.Str(required=True, validate=Views().validate_all_values)
