from flask import Flask
import flask
app = Flask(__name__)



@app.route('/login')
def hello_world():  # put application's code here
    return flask.render_template('login.html')


if __name__ == '__main__':
    app.run()
