from app import app
from db import db
from models import article, source

with app.app_context():
    db.create_all()

app.run()
