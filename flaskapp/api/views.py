from . import api_blueprint
from flask import jsonify
from ..main.api_calls import TfLAPICalls
from ..main.db_helpers import add_to_db, get_history
from datetime import datetime
from werkzeug.exceptions import HTTPException, TooManyRequests, NotFound

class Errors: 
    TFL_API_ERR = "There was a problem contacting TFL, please try again."
    TOO_MANY_REQ_ERR = "You have submitted too many requests. Please wait 10 mins before retrying."
    GENERIC_ERR = "An unknown error occurred while trying to contact TfL."
    NOT_FOUND_ERR = "TfL could not find that resource."

@api_blueprint.route("/live-arrivals/<smscode>")
def data(smscode):
    api = TfLAPICalls()
    try:
        stops = api.getStopsBySmsCode(smscode)
    except TooManyRequests as e:
        return(jsonify(error=Errors.TOO_MANY_REQ_ERR),e.get_response().status_code)
    except NotFound as e:
        return(jsonify(error=Errors.NOT_FOUND_ERR),e.get_response().status_code)
    except HTTPException as e:
        return(jsonify(error=Errors.TFL_API_ERR),e.get_response().status_code)
    except:
        return(jsonify(error=Errors.GENERIC_ERR),500)
    naptan_ids = stops[0]
    stop_letters = stops[1]
    common_names = stops[2]
    stops = []
    for index, naptan_id in enumerate(naptan_ids):
        try:
            response = api.getStopLiveArrivals(naptan_id)
        except TooManyRequests as e:
            return(jsonify(error=Errors.TOO_MANY_REQ_ERR),e.get_response().status_code)
        except NotFound as e:
            return(jsonify(error=Errors.NOT_FOUND_ERR),e.get_response().status_code)
        except HTTPException as e:
            return(jsonify(error=Errors.TFL_API_ERR),e.get_response().status_code)
        except:
            return(jsonify(error=Errors.GENERIC_ERR),500)
        filtered = list(filter(lambda item:item['modeName']=='bus', response))
        if len(filtered)>0:
            add_to_db(filtered, stop_letters[index])
            for item in filtered:
                now = datetime.today()
                expectedDatetime = datetime.strptime(item['expectedArrival'], '%Y-%m-%dT%H:%M:%SZ')
                item['expectedArrival'] = round((expectedDatetime-now).seconds/60)
                item['expectedArrivalString'] = str(item['expectedArrival'])+'m'
        sortedR = sorted(filtered, key=lambda item:item['expectedArrival'])
        arrivals = list(map(lambda response: {
                "lineName":response["lineName"],
                "destinationName":response["destinationName"],
                "expectedArrival":response["expectedArrivalString"]
            },sortedR))
        stops.append({
            "common_name":common_names[index],
            "stop_letter":stop_letters[index],
            "arrivals":arrivals
            })
    return jsonify(stops)

@api_blueprint.route("/live-arrivals/naptan/<naptan_id>")
def live_arrivals_naptan(naptan_id):
    api = TfLAPICalls()
    try:
        response = api.getStopLiveArrivals(naptan_id)
    except TooManyRequests as e:
        return(jsonify(error=Errors.TOO_MANY_REQ_ERR),e.get_response().status_code)
    except NotFound as e:
        return(jsonify(error=Errors.NOT_FOUND_ERR),e.get_response().status_code)
    except HTTPException as e:
        return(jsonify(error=Errors.TFL_API_ERR),e.get_response().status_code)
    except:
        return(jsonify(error=Errors.GENERIC_ERR),500)
    if len(response)>0:
        add_to_db(response, response[0]['platformName'])
        for item in response:
            now = datetime.today()
            expectedDatetime = datetime.strptime(item['expectedArrival'], '%Y-%m-%dT%H:%M:%SZ')
            item['expectedArrival'] = round((expectedDatetime-now).seconds/60)
            item['expectedArrivalString'] = str(item['expectedArrival'])+'m'
    sortedR = sorted(response, key=lambda item:item['expectedArrival'])
    arrivals = list(map(lambda response:{
            "lineName":response["lineName"],
            "destinationName":response["destinationName"],
            "expectedArrival":response["expectedArrivalString"]
    },sortedR))
    return jsonify([
        {
            "common_name":response[0]['stationName'],
            "arrivals":arrivals
        }
    ])

@api_blueprint.route("/get-history")
def gethistory():
    history = get_history()
    return jsonify(history)