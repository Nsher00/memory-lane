from flask import Flask, render_template
from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = 'superdupersecret'
app.jinja_env.undefined = StrictUndefined

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
