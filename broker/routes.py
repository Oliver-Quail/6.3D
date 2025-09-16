from dataclasses import dataclass

from flask import request, redirect
from flask.json import jsonify

from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import defer

from . import app, db
from .models import Hospital

import requests
from flask import Response


hospitals = ["http://127.0.0.1:5000", "http://127.0.0.1:4000", "http://127.0.0.1:4500"]


@app.route("/api/hospital", methods=["GET"])
def hospital():
    query = db.select(Hospital)
    hospital = db.session.execute(query).scalars()

    response = jsonify(hospital.all())
    return response

@app.route("/api/temp", methods=["GET"])
def temp():
    hospital = Hospital(name="Royal Melbourne", location="56 Royal street", total_beds=70, in_transit=3, occupied=66, has_burn_unit=50, has_icu=10, has_water_unit=0)
    db.session.add(hospital)
    hospital = Hospital(name="Hawthorn Hospital", location="100 Fenwick street", total_beds=900, in_transit=100, occupied=600, has_burn_unit=0, has_icu=0, has_water_unit=0)
    db.session.add(hospital)
    db.session.commit()
    return "meow"



@app.route("/api/update", methods=["GET"])
def update_service():

    for url in hospitals:
        update_hospital_data(url)


    return "meow"



def update_hospital_data(url):

    #requests.get("http://127.0.0.1:5000/api/hospital").content
    # Response(requests.get("http://127.0.0.1:5000/api/hospital").content, mimetype="application/json")
    try:
        response = requests.get(url + "/api/hospital").json()
    
    except:
        print("failed")
        return "failed"

    print("passed")
    query = db.select(Hospital).filter_by(name=response[0]["name"])
    res = db.session.execute(query).scalars()

    print(len(res.all()) == 0)


    if res.first() is None:
        print("Running") 
        hospital = Hospital(name=response[0]["name"], location=response[0]["location"], total_beds=response[0]["total_beds"], in_transit=response[0]["in_transit"], occupied=response[0]["occupied"], has_burn_unit=response[0]["has_burn_unit"], has_icu=response[0]["has_icu"], has_water_unit=response[0]["has_water_unit"])
        db.session.add(hospital)
        db.session.commit()
    else:
        Hospital.query.filter_by(name=response[0]["name"]).update({"total_beds": response[0]["total_beds"], "in_transit": response[0]["in_transit"], "occupied": response[0]["occupied"]})

        db.session.commit()

    return response[0]