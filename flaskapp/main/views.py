from . import main_blueprint
from flask import render_template
from .api_calls import TfLAPICalls
from .db_helpers import add_to_db, get_history
from datetime import datetime

@main_blueprint.route("/")
def index():
    api = TfLAPICalls()
    response = api.getStopLiveArrivals()
    if len(response)>0:
        add_to_db(response)
        for item in response:
            now = datetime.today()
            expectedDatetime = datetime.strptime(item['expectedArrival'], '%Y-%m-%dT%H:%M:%SZ')
            item['expectedArrival'] = round((expectedDatetime-now).seconds/60)
            item['expectedArrivalString'] = str(item['expectedArrival'])+'m'
    sortedR = sorted(response, key=lambda item:item['expectedArrival'])
    return render_template("main/home.html", response = sortedR)

@main_blueprint.route("/history")
def history():
    return render_template("main/history.html", requests = get_history())
