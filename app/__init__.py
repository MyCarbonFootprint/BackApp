from flask import Flask
from flasgger import Swagger
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
swagger = Swagger()


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
        if os.environ["FLASK_ENV"] == 'development':
            # Init Swagger
            Swagger(
                app,
                config={
                    "static_url_path": "/flasgger_static",
                    # URL to the documentation
                    "specs_route": "/documentation/",
                    "headers": [
                    ],
                    "specs": [
                        {
                            "endpoint": 'specifications',
                            "route": '/specifications.json',
                        }
                    ],
                },
                template_file=(
                    os.path.dirname(os.path.realpath(__file__)) +
                    '/resources/flasgger/template.json'
                )
        )

    return app
