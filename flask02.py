from flask import Flask, render_template
from flask_script import Manager

app = Flask(__name__)
manager = Manager(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)


from datetime import datetime
from flask_moment import Moment

moment = Moment(app)


@app.route('/indaa/')
def indaa():
    return render_template("index.html",
                           current_time=datetime.utcnow())


if __name__ == '__main__':
    manager.run()
