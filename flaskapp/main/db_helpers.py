from ..models import Request, ExpectedArrival
from datetime import datetime

def add_to_db(data, stop_name):
    request_time = datetime.strptime(data[0]['timing']['sent'], '%Y-%m-%dT%H:%M:%SZ')
    station_name = data[0]['stationName']
    naptan_id = data[0]['naptanId']
    platform_name = stop_name
    req = Request(request_time = request_time, station_name = station_name, naptan_id = naptan_id, platform_name = platform_name)
    for item in data:
        exp_arr_time = datetime.strptime(item['expectedArrival'], '%Y-%m-%dT%H:%M:%SZ')
        exp_arrival = ExpectedArrival(expected_arrival = exp_arr_time, line_name = item['lineName'], destination_name = item['destinationName'])
        req.expected_arrivals.append(exp_arrival)
    req.save()

def get_history():
    requests = []
    for request in Request.objects:
        expected_arrivals = []
        for expected_arrival in request.expected_arrivals:
            exp_arriv = round((expected_arrival.expected_arrival-request.request_time).seconds/60)
            expected_arrival_string = str(exp_arriv)+'m'
            expected_arrivals.append({
                'lineName':expected_arrival.line_name,
                'destinationName':expected_arrival.destination_name,
                'expectedArrival':expected_arrival_string,
                'expected_arrival_number':exp_arriv
            })
        arr_sorted = sorted(expected_arrivals, key=lambda item:item['expected_arrival_number'])
        requests.append({
            'common_name':request.station_name,
            'naptan_id':request.naptan_id,
            'stop_letter':request.platform_name,
            'request_date':request.request_time.strftime("%d %b %Y"),
            'request_time':request.request_time.strftime("%H:%M"),
            'arrivals':arr_sorted
        })
    return requests
