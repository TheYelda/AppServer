# coding=utf-8
"""Initialize `app` module."""

import os
from flask import Flask
from config import config
from .model import init_db

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


    from flask_login import LoginManager
    login_manager = LoginManager()
    login_manager.init_app(app)
    
    from .model import accounts
    @login_manager.user_loader
    def load_user(userid):
        return accounts.find_account_by_id(
                userid,
                lambda err: print(err),
                lambda accounts: accounts)

    from .api import api
    api.init_app(app)
    app.config['SECRET_KEY'] = 'Yelda is fxxking awesome'  

    return app

