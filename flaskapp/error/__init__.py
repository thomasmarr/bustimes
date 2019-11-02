from flask import Blueprint

error_blueprint = Blueprint("error", __name__)

from . import handler