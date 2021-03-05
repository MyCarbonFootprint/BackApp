import logging
import os

from flask import Blueprint, abort, jsonify, request

# Internal imports
from app.authentication.authentication import (
    check_token
)
from .ActionFamily import ActionFamily

action_family = Blueprint(
    'action_family', __name__, url_prefix='/v1/action_family'
)

log = logging.getLogger(__name__)

# Get current directory
dir_path = os.path.dirname(os.path.realpath(__file__))


# Get list
@action_family.route('', methods=['GET'])
@check_token()
def get_action_families():
    log.info("Get action family list")

    # Generate list
    action_families = ActionFamily.get_list()

    # Check
    if len(action_families) == 0:
        abort(400, {'message': 'No action family.'})

    return jsonify(action_families)


# Get
@action_family.route('/<string:id>', methods=['GET'])
@check_token()
def get_action_family(id):
    log.info("Get action family with id " + id)

    try:
        # Get action from id
        action_family = ActionFamily.get_by_id(id)
    except Exception as err:
        abort(404, {'message': str(err)})

    return jsonify(action_family.to_array())


# Create
@action_family.route('', methods=['POST'])
@check_token()
def create_action_family():
    log.info('Create action family')

    # Get JSON content received
    content = request.get_json(silent=True)

    # Check content
    check_content_attributs(content)

    # Create the id
    id_family = len(ActionFamily.get_list()) + 1

    # Create object
    action_family = ActionFamily(
        id=id_family,
        name=content['name'],
        description=content['description']
    )

    try:
        # format return
        content = action_family.to_array()
        # create
        action_family.create()
    except Exception as err:
        abort(409, {'message': str(err)})

    return (jsonify(content))


# Delete an action
@action_family.route('/<string:id>', methods=['DELETE'])
@check_token()
def delete_action_family(id):
    log.info("Delete action family " + id)

    try:
        # Get from id
        action_family = ActionFamily.get_by_id(id)
    except Exception as err:
        abort(404, {'message': str(err)})

    try:
        # delete
        action_family.delete()
    except Exception as err:
        abort(400, {'message': str(err)})

    return ('', 204)


@action_family.route('/<string:id>', methods=['PUT'])
@check_token()
def update_action(id):
    log.info("Update action family with the id " + id)

    # Get JSON content received
    content = request.get_json(silent=True)

    # Check content
    check_content_attributs(content)

    try:
        # Get from id
        action_family = ActionFamily.get_by_id(id)
    except Exception as err:
        abort(404, {'message': str(err)})

    new_action_family = ActionFamily(
        id=id,
        name=content['name'],
        description=content['description']
    )

    # Update
    try:
        # update
        action_family.update(new_action_family)
    except Exception as err:
        abort(406, {'message': str(err)})

    return jsonify(new_action_family.to_array())

def check_content_attributs(content):
    # Check if content is not empty
    if content is None:
        abort(406, {'message': 'No content'})

    # Check attributs
    if (
        'name' not in content or
        'description' not in content
    ):
        abort(406, {'message': 'Content not complete'})
