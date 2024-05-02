from db import db

class Reservation(db.Model):
    __tablename__ = "reservations"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    phone = db.Column(db.String(30))
    reservation_time = db.Column(db.Date())
    people = db.Column(db.Integer)
    requests = db.Column(db.Text)
