from flask import render_template
from . import error_blueprint
from werkzeug.exceptions import HTTPException

@error_blueprint.app_errorhandler(Exception)
def error_handler(error):
    if isinstance(error, HTTPException):
        error_code = error.code
    else:
        error_code=500
    try:
        description = error.description
    except AttributeError:
        description = None
    return render_template('error/error.html', error_code = error_code, description = description)