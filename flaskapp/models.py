from . import db

class Request(db.Model):
    __tablename__ = 'requests'
    id = db.Column(db.Integer, primary_key=True)
    request_time = db.Column(db.DateTime, nullable=False)
    station_name = db.Column(db.String, nullable=False)
    naptan_id = db.Column(db.String, nullable=False)
    platform_name = db.Column(db.String)
    expected_arrivals = db.relationship("ExpectedArrival", backref="request")

    def __repr__(self):
        return '<Request %r>' % self.id

class ExpectedArrival(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    expected_arrival = db.Column(db.DateTime, nullable=False)
    line_name = db.Column(db.String)
    destination_name = db.Column(db.String)
    request_id = db.Column(db.Integer, db.ForeignKey("requests.id"), nullable=False)

    def __repr__(self):
        return '<ExpectedArrival %r>' % self.id