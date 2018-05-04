# coding=utf-8
"""Provide common utilities for API processing."""

from flask import current_app

class DBErrorCodes(object):
    """
    Collect MySQL error codes that are used in this project.

    Refer to
    https://dev.mysql.com/doc/refman/8.0/en/error-messages-server.html
    """
    # Duplicate entry for unique key
    DUPLICATE_ENTRY = 1062


DB_ERR_CODES = DBErrorCodes()

class HttpCodes(object):
    OK = 200
    CREATED = 201
    NO_CONTENT = 204
    BAD_REQUEST = 400
    NOT_FOUND = 404 
    INTERNAL_SERVER_ERROR = 500

HTTPStatus = HttpCodes()

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
