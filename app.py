from flask import Flask
from datetime import datetime
import re
from flask import render_template
from flaskext.mysql import MySQL
from connect import connect
from get_all import get_all_patients
from get_one_patient import get_one_patient
from add_patient import insert_patient

app = Flask(__name__)
mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'F@guy1987'
app.config['MYSQL_DATABASE_DB'] = 'epilepsy_db'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

@app.route("/post/<first_name><last_name>")
def new_patient(first_name, last_name):
    print('in new patient, args are', first_name,last_name)
    insert_patient(first_name,last_name)
    data = get_all_patients()
    return render_template("patients.html", patients=data)

@app.route("/")
def patients():
    data = get_all_patients()
    return render_template("patients.html", patients=data)

@app.route("/single-patient/")
@app.route("/single-patient/<id>")
def single_patient(id = 0):
    data = get_one_patient(id)
    # print('in app, data is ', data)
    return render_template("single_patient.html", patient=data)

@app.route("/drugs/")
def drugs():
    return render_template("drugs.html")