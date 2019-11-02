from flask import current_app
import requests

class TfLAPICalls(object):
    def __init__(self):
        APP_ID = current_app.config['TFL_APP_ID']
        API_KEY = current_app.config['TFL_API_KEY']
        self.keys = {'app_id':APP_ID, 'app_key':API_KEY} 
    
    def getStopLiveArrivals(self):
        try:
            times = requests.get('https://api.tfl.gov.uk/StopPoint/490009333W/arrivals', params=self.keys)
            times.raise_for_status()
            return times.json()
        except requests.exceptions.HTTPError as e:
            print(e)
            return 'An error occurred while contacting TfL. ' + times.json()['message']
        except:
            return 'An unknown error occurred while contacting TfL.'
        