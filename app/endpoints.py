"""Contains the routes for the favour Blueprint."""
from flask import Blueprint, jsonify, request, g

from .exceptions import CustomError

favour = Blueprint('user', __name__)


@favour.route("/")
def index():
    """Index route."""
    return 'favour index'
