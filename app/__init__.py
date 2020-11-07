from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

from app.config import Config

import os


# Check if variables exists
def check_environment_variables(env_var_array):
    try:
        for variable in env_var_array:
            os.environ[variable]
    except KeyError:
        print("Please set the environment variable " + variable)
        exit(1)


# Check token
check_environment_variables(['API_TOKEN'])

# Initialize
db = SQLAlchemy(session_options={"expire_on_commit": False})


def create_app(config_class=Config):
    # create and configure the app
    app = Flask(__name__)
    CORS(app)

    # Use config
    app.config.from_object(config_class)

    # Import routes
    from .main.MainController import main
    from .main.VersionController import version
    from .errors.ErrorHandler import errors
    from .action.ActionController import action

    # Get blueprint by routes
    app.register_blueprint(errors)
    app.register_blueprint(main)
    app.register_blueprint(version)
    app.register_blueprint(action)

    with app.app_context():
        # Init db
        db.init_app(app)
        db.create_all()

    return app
