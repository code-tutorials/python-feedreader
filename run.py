from app import app
from db import db
from models import article, source
import routes

with app.app_context():
    db.create_all()

app.run()
