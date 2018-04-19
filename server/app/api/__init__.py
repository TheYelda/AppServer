# coding=utf-8
"""
Initialize `api` module.

Refer to http://flask-restplus.readthedocs.io/en/stable/scaling.html
"""
from flask_restplus import Api

from .account import api as account_ns

api = Api(
    title='Yelda',
    version='1.0'
)

# `path` is somehow required
api.add_namespace(account_ns, path='/accounts')
