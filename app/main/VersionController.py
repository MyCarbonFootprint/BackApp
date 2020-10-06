from flask import Blueprint

version = Blueprint('version', __name__)


@version.route('/v1')
def index_v1():
    return "<h1>Welcome to my API Version 1.</h1>"
