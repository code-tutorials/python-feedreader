from db import db
import datetime

class Source(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text, nullable=False)
    subtitle = db.Column(db.Text, nullable=False)
    link = db.Column(db.Text, nullable=False)
    feed = db.Column(db.Text, nullable=False)
    date_added = db.Column(db.DateTime, default=datetime.datetime.utcnow)
