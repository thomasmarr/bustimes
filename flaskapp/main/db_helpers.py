from .. import db
from ..models import Request, ExpectedArrival
from datetime import datetime

def add_to_db(data):
    request_time = datetime.strptime(data[0]['timing']['sent'], '%Y-%m-%dT%H:%M:%SZ')
    station_name = data[0]['stationName']
    naptan_id = data[0]['naptanId']
    req = Request(request_time = request_time, station_name = station_name, naptan_id = naptan_id)
    for item in data:
        exp_arr_time = datetime.strptime(item['expectedArrival'], '%Y-%m-%dT%H:%M:%SZ')
        exp_arrival = ExpectedArrival(expected_arrival = exp_arr_time, line_name = item['lineName'], destination_name = item['destinationName'], request_id=req.id)
        req.expected_arrivals.append(exp_arrival)
        db.session.add(exp_arrival)
    db.session.add(req)
    db.session.commit()

def get_history():
    query = Request.query.order_by(Request.request_time.desc()).options(db.joinedload('expected_arrivals'))
    requests = []
    for request in query:
        expected_arrivals = []
        for expected_arrival in request.expected_arrivals:
            exp_arriv = round((expected_arrival.expected_arrival-request.request_time).seconds/60)
            expected_arrival_string = str(exp_arriv)+'m'
            expected_arrivals.append({
                'line_name':expected_arrival.line_name,
                'destination_name':expected_arrival.destination_name,
                'expected_arrival_string':expected_arrival_string,
                'expected_arrival_number':exp_arriv
            })
        arr_sorted = sorted(expected_arrivals, key=lambda item:item['expected_arrival_number'])
        requests.append({
            'station_name':request.station_name,
            'naptan_id':request.naptan_id,
            'request_date':request.request_time.strftime("%d %b %Y"),
            'request_time':request.request_time.strftime("%H:%M"),
            'expected_arrivals':arr_sorted
        })
    return requests