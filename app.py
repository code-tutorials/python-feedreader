from flask import Flask

app = Flask(__name__)
db_uri = 'mysql+pymysql://root:password@localhost/feedreader'
app.config['SQLALCHEMY_DATABASE_URI'] = db_uri