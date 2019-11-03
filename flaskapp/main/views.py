from . import main_blueprint
from flask import render_template, request, redirect, url_for
from .api_calls import TfLAPICalls
from .db_helpers import add_to_db, get_history
from datetime import datetime

@main_blueprint.route("/")
def index():
    api = TfLAPICalls()
    response = api.getStopLiveArrivals('490009333W')
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

@main_blueprint.route("/live-arrivals/<naptan_id>")
def live_arrivals(naptan_id):
    api = TfLAPICalls()
    response = api.getStopLiveArrivals(naptan_id)
    filtered = list(filter(lambda item:item['modeName']=='bus', response))
    if len(filtered)>0:
        add_to_db(filtered)
        for item in filtered:
            now = datetime.today()
            expectedDatetime = datetime.strptime(item['expectedArrival'], '%Y-%m-%dT%H:%M:%SZ')
            item['expectedArrival'] = round((expectedDatetime-now).seconds/60)
            item['expectedArrivalString'] = str(item['expectedArrival'])+'m'
    sortedR = sorted(filtered, key=lambda item:item['expectedArrival'])
    return render_template("main/home.html", response = sortedR)

@main_blueprint.route("/live-arrivals", methods = ['GET','POST'])
def live_arrivals_form():
    if request.method == 'GET':
        return render_template("main/sms.html")
    sms_code = request.form.get('smscode')
    api = TfLAPICalls()
    naptan_id = api.getNaptanIdBySmsCode(sms_code)
    return redirect(url_for('main.live_arrivals', naptan_id = naptan_id))
