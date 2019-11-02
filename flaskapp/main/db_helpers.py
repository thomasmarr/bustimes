from .. import db
from ..models import Request, ExpectedArrival
from datetime import datetime

def add_to_db(data):
    request_time = datetime.strptime(data[0]['timing']['sent'], '%Y-%m-%dT%H:%M:%SZ')
    req = Request(request_time = request_time)
    for item in data:
        exp_arr_time = datetime.strptime(item['expectedArrival'], '%Y-%m-%dT%H:%M:%SZ')
        exp_arrival = ExpectedArrival(expected_arrival = exp_arr_time, line_name = item['lineName'], destination_name = item['destinationName'], request_id=req.id)
        req.expected_arrivals.append(exp_arrival)
        db.session.add(exp_arrival)
    db.session.add(req)
    db.session.commit()