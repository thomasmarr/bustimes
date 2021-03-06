from flask import current_app
from werkzeug.exceptions import abort, TooManyRequests, NotFound
import requests

class TfLAPICalls(object):
    def __init__(self):
        APP_ID = current_app.config['TFL_APP_ID']
        API_KEY = current_app.config['TFL_API_KEY']
        self.keys = {'app_id':APP_ID, 'app_key':API_KEY} 
    
    def getStopLiveArrivals(self, naptan_id):
        try:
            times = requests.get(f'https://api.tfl.gov.uk/StopPoint/{naptan_id}/arrivals', params=self.keys)
            times.raise_for_status()
            return times.json()
        except requests.exceptions.HTTPError as e:
            print(e)
            if e.response.status_code == 429:
                raise TooManyRequests()
            elif e.response.status_code == 404:
                raise NotFound()
            else:
                abort(e.response.status_code, 'An error occurred while contacting TfL. ' + times.json()['message'])
        except:
            raise Exception()

    def getStopsBySmsCode(self, sms_code):
        try:
            stopPoint = requests.get(f'https://api.tfl.gov.uk/StopPoint/Sms/{sms_code}', params=self.keys)
            stopPoint.raise_for_status()
            naptanIds = []
            stopNames = []
            commonNames = []
            for child in stopPoint.json()['children']:
                naptanIds.append(child['naptanId'])
                stopNames.append(child['indicator'])
                commonNames.append(child['commonName'])
            return [naptanIds, stopNames, commonNames]
        except requests.exceptions.HTTPError as e:
            print(e)
            if e.response.status_code == 429:
                raise TooManyRequests()
            elif e.response.status_code == 404:
                raise NotFound()
            else:
                abort(e.response.status_code, 'An error occurred while contacting TfL. ' + times.json()['message'])
        except:
            raise Exception()