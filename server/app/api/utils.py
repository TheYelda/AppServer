# coding=utf-8
"""Provide common utilities for API processing."""
from flask import current_app
from http import HTTPStatus


class DBErrorCodes(object):
    """
    Collect MySQL error codes that are used in this project.

    Refer to
    https://dev.mysql.com/doc/refman/8.0/en/error-messages-server.html
    """
    # Duplicate entry for unique key
    DUPLICATE_ENTRY = 1062
    # Foreign key failes
    FOREIGN_KEY_FAILURE = 1452


class ConstantCodes(object):
    """Constant codes for some states."""
    # Authority 1XX
    Empty = 100
    Admin = 101
    Doctor = 102
    Guest = 103
    # Job State 2XX
    Unlabeled = 200
    Labeling = 201
    Finished = 202
    # Image State 3XX
    Unassigned = 300
    Running = 301
    Different = 302
    Done = 303


def get_message_json(message):
    """Return a json with message."""
    return {'message': message}


def handle_internal_error(message):
    """
    Log unknown error and return tuple of json and status code.
    :param message: error message
    :return: tuple of json and status code
    """
    current_app.logger.exception(message)
    return get_message_json('服务器内部错误'), HTTPStatus.INTERNAL_SERVER_ERROR


def convert_to_int(argument):
    """
    A helper function to convert argument in the query string into int.
    :param argument: the string-type argument got by `request.args.get('...')`
    :return: the corresponding int or None
    """
    return int(argument) if argument else None

def convert_to_int_default0(argument):
    """
    A helper function to convert argument in the query string into int.
    :param argument: the string-type argument got by `request.args.get('...')`
    :return: the corresponding int or 0
    """
    return int(argument) if argument else 0
