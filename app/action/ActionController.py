import logging
import os

from flask import Blueprint, abort, jsonify, request

# Internal imports
from app.authentication.authentication import (
    check_token
)
from .Action import Action

action = Blueprint(
    'action', __name__, url_prefix='/v1/action'
)

log = logging.getLogger(__name__)

# Get current directory
dir_path = os.path.dirname(os.path.realpath(__file__))


# Get action list
@action.route('', methods=['GET'])
@check_token()
def get_actions():
    log.info("Get action list")

    # Generate action list
    actions = Action.get_list()

    # Check
    if len(actions) == 0:
        abort(400, {'message': 'No action.'})

    return jsonify(actions)


# Get action
@action.route('/<string:id>', methods=['GET'])
@check_token()
def get_action(id):
    log.info("Get action with id " + id)

    try:
        # Get action from id
        action = Action.get_by_id(id)
    except Exception as err:
        abort(404, {'message': str(err)})

    return jsonify(action.to_array())


# Create a action
@action.route('', methods=['POST'])
@check_token()
def create_action():
    log.info('Create action')

    # Get JSON content received
    content = request.get_json(silent=True)

    # Check content
    check_content_attributs(content)

    # Create the id
    id = len(Action.get_list()) + 1

    # Create action object
    action = Action(
        id=id,
        name=content['name'],
        description=content['description'],
        unit=content['unit'],
        number=content['number'],
        impact=content['impact']
    )

    try:
        # format return
        content = action.to_array()
        # create
        action.create()
    except Exception as err:
        abort(409, {'message': str(err)})

    return (jsonify(content))


# Delete an action
@action.route('/<string:id>', methods=['DELETE'])
@check_token()
def delete_action(id):
    log.info("Delete action " + id)

    try:
        # Get action from id
        action = Action.get_by_id(id)
    except Exception as err:
        abort(404, {'message': str(err)})

    try:
        # delete
        action.delete()
    except Exception as err:
        abort(400, {'message': str(err)})

    return ('', 204)


@action.route('/<string:id>', methods=['PUT'])
@check_token()
def update_action(id):
    log.info("Update action with the id " + id)

    # Get JSON content received
    content = request.get_json(silent=True)

    # Check content
    check_content_attributs(content)

    try:
        # Get action from id
        action = Action.get_by_id(id)
    except Exception as err:
        abort(404, {'message': str(err)})

    new_action = Action(
        id=id,
        name=content['name'],
        description=content['description'],
        unit=content['unit'],
        number=content['number'],
        impact=content['impact']
    )

    # Update action
    try:
        # update
        action.update(new_action)
    except Exception as err:
        abort(406, {'message': str(err)})

    return jsonify(new_action.to_array())


@action.route('/impact', methods=['GET'])
@check_token()
def calcul_impact():
    log.info("Calcul impact")

    # Get JSON content received
    content = request.get_json(silent=True)

    # Get JSON content received
    # content = request.get_json(silent=True)
    if content is None:
        abort(406, {'message': 'No content'})

    # Check JSON keys
    # Another method sets the password
    if (
        not isinstance(content, list) and
        len(content) == 0
    ):
        abort(406, {'message': 'Content not complete'})

    total_impact = 0
    # Calcul total impact
    try:
        for daily_action in content:
            # Get action from id
            action = Action.get_by_id(daily_action["id"])
            # Add impact
            total_impact = total_impact + action.impact*daily_action["coef"]
    except Exception as err:
        abort(404, {'message': str(err)})

    return jsonify({
        "daily_impact": total_impact,
        "factors": [
            {
                "id": 7,
                "factor": total_impact/(Action.get_by_id(7).impact)
            },
            {
                "id": 2,
                "factor": total_impact/(Action.get_by_id(17).impact)
            }
        ]
    })

def check_content_attributs(content):
    # Check if content is not empty
    if content is None:
        abort(406, {'message': 'No content'})

    # Check attributs
    if (
        'name' not in content or
        'description' not in content or
        'unit' not in content or
        'number' not in content or
        'impact' not in content
    ):
        abort(406, {'message': 'Content not complete'})
