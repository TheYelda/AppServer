# coding=utf-8
"""Initialize `app` module."""

from flask import Flask
from config import config
from .model import init_db
import os


def create_app(config_name):
    """
    Create the app object.
    :param config_name: type of configuration
    :return: the app object
    """
    app = Flask(__name__, instance_relative_config=True)
    # Load public config
    app.config.from_object(config[config_name])
    # Load private config at instance/config.py
    if os.path.exists('instance/config.py'):
        app.config.from_pyfile('config.py')

    # Initialize database
    try:
        init_db(
            app.config['DB_USERNAME'],
            app.config['DB_PASSWORD'],
            app.config['DB_NAME']
        )
    except Exception as err:
        print(err)
        print('You have to configure your correct MySQL account in server/instance/config.py')
        exit(-1)

    from .api import api
    api.init_app(app)

    return app
