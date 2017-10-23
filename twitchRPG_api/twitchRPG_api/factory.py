from flask import Flask

from twitchRPG_api.views.base import base_api


def create_app():
    """
    Creates Flask app, adds all views registering via blueprint on '/' route
    """
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    app.register_blueprint(base_api)
    return app
