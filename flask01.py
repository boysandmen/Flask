

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

if __name__ == '__main__':
    app.run(debug=True)