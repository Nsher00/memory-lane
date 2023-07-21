from flask import Flask, render_template
from jinja2 import StrictUndefined
from forms import LoginForm
from json import JSONEncoder

app = Flask(__name__)
app.secret_key = 'superdupersecret'
app.jinja_env.undefined = StrictUndefined

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST', 'GET'])
def login():
    login_form = LoginForm()
    return render_template('login.html', login_form = login_form)

if __name__ == "__main__":
    app.run(debug=True)
