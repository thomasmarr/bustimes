from . import mongodb

class ExpectedArrival(mongodb.EmbeddedDocument):
    expected_arrival = mongodb.DateTimeField(required=True)
    line_name = mongodb.StringField()
    destination_name = mongodb.StringField()

class Request(mongodb.Document):
    request_time = mongodb.DateTimeField(required=True)
    station_name = mongodb.StringField(required=True)
    naptan_id = mongodb.StringField(required=True)
    platform_name = mongodb.StringField()
    expected_arrivals = mongodb.ListField(mongodb.EmbeddedDocumentField(ExpectedArrival))
