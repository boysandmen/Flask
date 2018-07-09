from flask import Flask


app = Flask(__name__)


@app.route('/user/<name>')
def index(name):
    return '<h1>Hello %s </h1>' % name


from flask import request


@app.route('/index')
def index_too():
    user_agent = request.headers.get('User-Agent')
    return '<p>Your browser is %s</p>' % user_agent


@app.route('/index_bad')
def index_bad():
    return '<h1>Bad Request</h1>', 400


from flask import make_response


@app.route('/')
def index_cookie():
    response = make_response('<h1>This document carries a cookie!</h1>')
    response.set_cookie('answer', '42')
    return response



if __name__ == '__main__':
    app.run(debug=True)
