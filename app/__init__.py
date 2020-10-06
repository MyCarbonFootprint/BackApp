from flask import Flask
from flasgger import Swagger

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
swagger = Swagger()


def create_app(config_class=Config):
    # create and configure the app
    app = Flask(__name__)

    # Use config
    app.config.from_object(config_class)

    # Import routes
    from .main.MainController import main
    from .main.VersionController import version
    from .errors.ErrorHandler import errors

    # Get blueprint by routes
    app.register_blueprint(errors)
    app.register_blueprint(main)
    app.register_blueprint(version)

    with app.app_context():
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
