from db import db
import datetime

class Source(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text, nullable=False)
    subtitle = db.Column(db.Text, nullable=False)
    link = db.Column(db.Text, nullable=False)
    feed = db.Column(db.Text, nullable=False)
    date_added = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    @classmethod
    def insert_from_feed(cls, feed, feed_source):
        link = feed_source['link']
        title = feed_source['title']
        subtitle = feed_source['subtitle']
        source = Source(feed=feed, link=link, title=title, subtitle=subtitle)
        db.session.add(source)
        db.session.commit()
        return source