from flask import Flask,render_template
from scraper import sendTemperatures
import json

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html',temperatures=sendTemperatures())

@app.route('/about')
def collectTemp():
    return '<h1>About Page</h1>'

@app.route('/ajaxCall')
def ajaxCall():
    return json.dumps(sendTemperatures())

if __name__ == "__main__":
    app.run(debug=True)
