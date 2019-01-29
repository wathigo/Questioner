""" import third party modules """
from marshmallow import Schema, fields
from .validators import Views


class UserValidate(Schema):
    """ Validate data for user registration """
    firstname = fields.Str(required=True, validate=Views().validate_all_values)
    lastname = fields.Str(required=True, validate=Views().validate_all_values)
    email = fields.Str(required=True, validate=Views().validate_email)
    password = fields.Str(required=True, validate=Views().validate_password)
    repeatpassword = fields.Str(required=True)
    othername = fields.Str(required=True)
    phonenumber = fields.Str(required=True)


class MeetupValidate(Schema):
    """ Validate data for meetup creation """
    title = fields.Str(required=True, validate=Views().validate_all_values)
    description = fields.Str(required=True, validate=Views().validate_all_values)
    date = fields.Date(required=True, validate=Views().validate_date)
    location = fields.Str(required=True, validate=Views().validate_all_values)


class QuestionValidate(Schema):
    """ Validate data for question creation """
    question = fields.Str(required=True, validate=Views().validate_all_values)


class ReserveValidate(Schema):
    """ Validate data for meetup reserve endpoint """
    status = fields.Str(required=True, validate=Views().validate_reserve)


class CommentValidate(Schema):
    """ Validators for comment creation"""
    comment = fields.Str(required=True)
