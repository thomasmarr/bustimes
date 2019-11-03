from . import main_blueprint
from flask import render_template, request, redirect, url_for
from .api_calls import TfLAPICalls
from .db_helpers import add_to_db, get_history
from datetime import datetime

@main_blueprint.route("/", methods = ['GET','POST'])
def index():
    if request.method == 'GET':
        return render_template("main/home.html")
    sms_code = request.form.get('smscode')
    api = TfLAPICalls()
    stops = api.getStopsBySmsCode(sms_code)
    cs_ids = ','.join(stops[0])
    cs_stops = ','.join(stops[1])
    cs_names = ','.join(stops[2])
    return redirect(url_for('main.live_arrivals', ids = cs_ids, stops = cs_stops, names = cs_names))

@main_blueprint.route("/live-arrivals/<naptan_id>")
def live_arrivals_naptan(naptan_id):
    api = TfLAPICalls()
    response = api.getStopLiveArrivals(naptan_id)
    if len(response)>0:
        add_to_db(response, response[0]['platformName'])
        for item in response:
            now = datetime.today()
            expectedDatetime = datetime.strptime(item['expectedArrival'], '%Y-%m-%dT%H:%M:%SZ')
            item['expectedArrival'] = round((expectedDatetime-now).seconds/60)
            item['expectedArrivalString'] = str(item['expectedArrival'])+'m'
    sortedR = sorted(response, key=lambda item:item['expectedArrival'])
    return render_template("main/naptan.html", response = sortedR)

@main_blueprint.route("/live-arrivals")
def live_arrivals():
    api = TfLAPICalls()
    stops = []
    naptan_ids = request.args.get('ids', '').split(',')
    stop_letters = request.args.get('stops', '').split(',')
    common_names = request.args.get('names', '').split(',')
    for index, naptan_id in enumerate(naptan_ids):
        print(naptan_id)
        response = api.getStopLiveArrivals(naptan_id)
        filtered = list(filter(lambda item:item['modeName']=='bus', response))
        if len(filtered)>0:
            add_to_db(filtered, stop_letters[index])
            for item in filtered:
                now = datetime.today()
                expectedDatetime = datetime.strptime(item['expectedArrival'], '%Y-%m-%dT%H:%M:%SZ')
                item['expectedArrival'] = round((expectedDatetime-now).seconds/60)
                item['expectedArrivalString'] = str(item['expectedArrival'])+'m'
        sortedR = sorted(filtered, key=lambda item:item['expectedArrival'])
        stops.append({
            "common_name":common_names[index],
            "stop_letter":stop_letters[index],
            "response":sortedR
            })
    return render_template("main/stops.html", response = stops)

@main_blueprint.route("/history")
def history():
    return render_template("main/history.html", requests = get_history())


