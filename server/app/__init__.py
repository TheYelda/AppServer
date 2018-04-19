# coding=utf-8
"""Initialize `app` module."""

from flask import Flask
from config import config
from .api import api


def create_app(config_name):
    """
    Create the app object.

    :param config_name: type of configuration
    :return: the app object
    """
    app = Flask(__name__, instance_relative_config=True)
    # load public config
    app.config.from_object(config[config_name])
    # load private config at instance/config.py
    # app.config.from_pyfile('config.py')

    api.init_app(app)

    return app
