# services/aktiver/project/__init__.py


import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

#import sentry_sdk
#from sentry_sdk.integrations.flask import FlaskIntegration

# instantiate the extensions
db = SQLAlchemy()
cors = CORS()


def create_app(script_info=None):

    # Initialize Sentry.io
    #sentry_sdk.init(
    #    dsn="http://bb28b1aa56e8475e964719f4f3416e63@sentry:9000/1",
    #    integrations=[FlaskIntegration()]
    #)

    # instantiate the app
    app = Flask(__name__)

    # set config
    app_settings = os.getenv("APP_SETTINGS")
    app.config.from_object(app_settings)

    # set up extensions
    db.init_app(app)
    cors.init_app(app, resources={r"*": {"origins": "*"}})

    # register api
    from project.api import api

    api.init_app(app)

    # shell context for flask cli
    @app.shell_context_processor
    def ctx():
        return {"app": app, "db": db}

    return app
