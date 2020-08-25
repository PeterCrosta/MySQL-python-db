from flask import Flask
from datetime import datetime
import re
from flask import render_template
from flaskext.mysql import MySQL
from connect import connect
from get_all import get_all_patients
from get_one_patient import get_one_patient

app = Flask(__name__)
mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'F@guy1987'
app.config['MYSQL_DATABASE_DB'] = 'epilepsy_db'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

@app.route("/api/data")
def get_data():
    return app.send_static_file("data.json")

@app.route("/")
def patients():
    data = get_all_patients()
    print('are we out of home func call? ------------')
    return render_template("patients.html", patients=data)

@app.route("/hello/<name>") # <name> creates a passed variable to be used in the func
def hello_there(name = None):
    return render_template(
        "hello_there.html",
        name=name,
        date=datetime.now()
    )


@app.route("/single-patient/")
def single_patient():
    data = get_one_patient()
    # print('in app, data is ', data)
    return render_template("single_patient.html", patient=data)

@app.route("/drugs/")
def drugs():
    return render_template("drugs.html")