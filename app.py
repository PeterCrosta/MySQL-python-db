from flask import Flask
from datetime import datetime
import re
from flask import render_template

app = Flask(__name__)

@app.route("/api/data")
def get_data():
    return app.send_static_file("data.json")

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/hello/<name>") # <name> creates a passed variable to be used in the func
def hello_there(name = None):
    return render_template(
        "hello_there.html",
        name=name,
        date=datetime.now()
    )


@app.route("/about/")
def about():
    return render_template("about.html")

@app.route("/contact/")
def contact():
    return render_template("contact.html")