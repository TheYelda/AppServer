# coding=utf-8
"""Provide common utilities for API processing."""


class HTTPStatusCodes(object):
     """
    Collect HTTP status codes that are used in this project.

#     Refer to
#     https://github.com/TheYelda/Dashboard/blob/master/http_status_codes_reference.md
#     """


     # 2xx: successful
     OK = 200
     CREATED = 201

     # 4xx: client error
     BAD_REQUEST = 400
    CONFLICT = 409



class DBErrorCodes(object):
    """
    Collect MySQL error codes that are used in this project.

    Refer to
    https://dev.mysql.com/doc/refman/8.0/en/error-messages-server.html
    """
    # Duplicate entry for unique key
    DUPLICATE_ENTRY = 1062


# HTTP_CODES = HTTPStatusCodes()
DB_ERR_CODES = DBErrorCodes()


def get_message_json(message):
    """Return a json with message."""
    return {'message': message}
