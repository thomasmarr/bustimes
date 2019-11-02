from . import main_blueprint
from flask import render_template
from .api_calls import TfLAPICalls


@main_blueprint.route("/")
def index():
    api = TfLAPICalls()
    response = api.getStopLiveArrivals()
    return render_template("main/home.html", response = response)
