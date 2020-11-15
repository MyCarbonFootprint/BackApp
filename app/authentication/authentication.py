import base64
import os

from flask import abort, request
from functools import wraps


# This decorator permits to the decorator check_rights
# to admit arguments
def parametrized(dec):
    def layer(*args, **kwargs):
        def repl(f):
            return dec(f, *args, **kwargs)
        return repl
    return layer


# Use decorator parametrized to permit to have arguments
@parametrized
def check_token(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        # If env is dev, no check
        if os.environ['FLASK_ENV'] == 'development':
            return f(*args, **kwargs)

        # Get TOKEN
        api_key = get_authorization_header()

        # Check Token
        if api_key != 'Basic ' + os.environ['API_TOKEN']:
            abort(
                401,
                {
                    'message': 'You do not have the permissions for this action.'
                }
            )

        # Run the function f if rights are ok
        return f(*args, **kwargs)
    return decorated_function

# Get Authorization header
def get_authorization_header():
    api_key = request.headers.get('Authorization')
    # Check if no token exists
    if not api_key:
        abort(
            401,
            {
                'message': 'You do not have the permissions for this action.'
            }
        )
    return api_key
