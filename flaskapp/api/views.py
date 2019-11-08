from . import api_blueprint
from flask import jsonify

@api_blueprint.route("/data")
def data():
    return jsonify(key="value")
