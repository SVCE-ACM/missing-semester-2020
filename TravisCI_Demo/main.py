from flask import Flask,request,jsonify
from flask_basicauth import BasicAuth

app = Flask(__name__)
app.config['BASIC_AUTH_USERNAME'] = 'travisci'
app.config['BASIC_AUTH_PASSWORD'] = 'tutorial'
basic_auth = BasicAuth(app)

@app.route("/")
def hello():
    return "Hello World!"

@app.route('/multiply')
def multiply():
    x = int(request.args.get('x'))
    y = int(request.args.get('y'))
    return jsonify({'answer':x*y})

@app.route('/touppercase')
def touppercase():
    string = request.args.get('s')
    return string.upper()


@app.route('/authorized')
@basic_auth.required
def authorized():
    return 'You are logged in'

if __name__ == '__main__':
    app.run()