from flask import Flask, render_template
from utils import fetch_sms

app = Flask(__name__)


@app.route("/")
def index():
    sms = fetch_sms()
    return render_template("index.html", sms=sms)
