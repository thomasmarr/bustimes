from . import main_blueprint
from flask import render_template
from .api_calls import TfLAPICalls
from datetime import datetime
from dateutil.parser import isoparse

@main_blueprint.route("/")
def index():
    api = TfLAPICalls()
    response = api.getStopLiveArrivals()
    for item in response:
        now = datetime.today()
        expectedDatetime = datetime.strptime(item['expectedArrival'], '%Y-%m-%dT%H:%M:%SZ')
        item['expectedArrival'] = round((expectedDatetime-now).seconds/60)
        item['expectedArrivalString'] = str(item['expectedArrival'])+'m'
    sortedR = sorted(response, key=lambda item:item['expectedArrival'])
    return render_template("main/home.html", response = sortedR)
