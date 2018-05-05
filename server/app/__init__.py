# coding=utf-8
"""Initialize `app` module."""
import os
from flask import Flask
from config import config
from .model import init_db
import logging
from logging.handlers import RotatingFileHandler

log_file = './log/exception.log'
log_mode = logging.DEBUG


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

    from .api import api
    api.init_app(app)

    # In case that the log directory has not been created
    log_dir = os.path.dirname(log_file)
    if not os.path.exists(log_dir):
        os.mkdir(log_dir)

    handler = RotatingFileHandler(log_file, maxBytes=1024 * 1024, backupCount=5)
    fmt = '%(asctime)s - %(filename)s:%(lineno)s - func: [%(name)s] - %(message)s'
    
    formatter = logging.Formatter(fmt)
    handler.setFormatter(formatter)

    app.logger.addHandler(handler)
    app.logger.setLevel(log_mode)
    
    return app

