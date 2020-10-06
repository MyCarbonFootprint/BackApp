from flask import Blueprint, jsonify, make_response

errors = Blueprint('errors', __name__)


# Error 400
@errors.app_errorhandler(400)
def not_found(error):
    if 'message' in error.description:
        return make_response(
            jsonify(
                {'error': error.description['message']}
            ), 400
        )
    else:
        return make_response(
            jsonify(
                {'error': 'Not found'}
            ), 400
        )


# Error 401
@errors.app_errorhandler(401)
def access_denied(error):
    if 'message' in error.description:
        return make_response(
            jsonify(
                {'error': error.description['message']}
            ), 401
        )
    else:
        return make_response(
            jsonify(
                {'error': 'Access Denied'}
            ), 401
        )


# Error 403
@errors.app_errorhandler(403)
def forbidden(error):
    if 'message' in error.description:
        return make_response(
            jsonify(
                {'error': error.description['message']}
            ), 403
        )
    else:
        return make_response(
            jsonify(
                {'error': 'Forbidden'}
            ), 403
        )


# Error 404
@errors.app_errorhandler(404)
def bad_request(error):
    if 'message' in error.description:
        return make_response(
            jsonify(
                {'error': error.description['message']}
            ), 404
        )
    else:
        return make_response(
            jsonify(
                {'error': 'Bad request'}
            ), 404
        )


# Error 405
@errors.app_errorhandler(405)
def not_allowed(error):
    if 'message' in error.description:
        return make_response(
            jsonify(
                {'error': error.description['message']}
            ), 405
        )
    else:
        return make_response(
            jsonify(
                {'error': 'Method not allowed'}
            ), 405
        )


# Error 406
@errors.app_errorhandler(406)
def not_acceptable(error):
    if 'message' in error.description:
        return make_response(
            jsonify(
                {'error': error.description['message']}
            ), 406
        )
    else:
        return make_response(
            jsonify(
                {"error": "Not Acceptable"}
            ), 406
        )


# Error 409
@errors.app_errorhandler(409)
def conflict(error):
    if 'message' in error.description:
        return make_response(
            jsonify(
                {'error': error.description['message']}
            ), 409
        )
    else:
        return make_response(
            jsonify(
                {"error": "Resource already exists"}
            ), 409
        )
