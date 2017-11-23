from flask import redirect, request
from app import app

@app.route('/test', methods=['GET'])
def test_get():
    return '<form method="POST"><input name="username"></form>'

@app.route('/test', methods=['POST'])
def test_post():
    username = request.form.get('username', '???')
    return 'Hello ' + username