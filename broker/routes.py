from dataclasses import dataclass

from flask import request, redirect
from flask.json import jsonify

from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import defer

from . import app, db
from .models import Hospital

import requests
from flask import Response



@app.route("/api/hospital", methods=["GET"])
def hospital():
    query = db.select(Hospital)
    hospital = db.session.execute(query).scalars()

    response = jsonify(hospital.all())
    return response



@app.route("/api/test", methods=["GET"])
def test():

    #requests.get("http://127.0.0.1:5000/api/hospital").content
    # Response(requests.get("http://127.0.0.1:5000/api/hospital").content, mimetype="application/json")
    
    response = requests.get("http://127.0.0.1:5000/api/hospital").json()


    query = db.select(Hospital).filter_by(name=response[0]["name"])
    res = db.session.execute(query).scalars()

    print(len(res.all()) == 0)


    if res.first is None:
        print("Running")
        hospital = Hospital(name=response[0]["name"], location=response[0]["location"], total_beds=response[0]["total_beds"], in_transit=response[0]["in_transit"], occupied=response[0]["occupied"])
        db.session.add(hospital)
        db.session.commit()
    else:
        Hospital.query.filter_by(name=response[0]["name"]).update({"total_beds": response[0]["total_beds"], "in_transit": response[0]["in_transit"], "occupied": response[0]["occupied"]})

        db.session.commit()

    return response[0]