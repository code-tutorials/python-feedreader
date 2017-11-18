from db import db
import datetime

class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text, nullable=False)
    body = db.Column(db.Text, nullable=False)
    link = db.Column(db.Text, nullable=False)
    guid = db.Column(db.String(255), nullable=False)
    unread = db.Column(db.Boolean, default=True, nullable=False)
    source_id = db.Column(db.Integer, db.ForeignKey('source.id'), nullable=False)
    source = db.relationship('Source', db.backref('articles', lazy=True))
    date_added = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    date_published = db.Column(db.DateTime)
    __table_args__ = (
        db.UniqueConstraint('source_id', 'guid', name='uc_source_guid'),
    )