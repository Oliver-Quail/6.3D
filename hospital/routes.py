from dataclasses import dataclass

from flask import request, redirect
from flask.json import jsonify

from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import defer

from . import app, db
from .models import Hospital

@app.route("/api/init", methods=["GET"])
def temp():
    hospital = Hospital(name="Burwood", location="123 street", total_beds=100, in_transit=40, occupied=30,  has_burn_unit=10, has_icu=20, has_water_unit=5)
    db.session.add(hospital)
    db.session.commit()
    return "meow"


@app.route("/api/hospital", methods=["GET"])
def hospital():
    query = db.select(Hospital)
    hospital = db.session.execute(query).scalars()

    response = jsonify(hospital.all())
    return response


@app.route("/api/assign", methods=["GET"])
def assign():
    query = db.select(Hospital.total_beds, Hospital.in_transit, Hospital.occupied)
    res = db.session.execute(query).first()
    print(res)
    max_beds = res.total_beds

    if max_beds - res.in_transit - res.occupied <= 0:
        return "error"
    
    h = db.session.query(Hospital).first()
    h.in_transit = h.in_transit + 1
    db.session.commit()
    
    return str(max_beds - (res.in_transit + res.occupied))


@app.route("/api/deassign", methods=["GET"])
def deassign():
    h = db.session.query(Hospital).first()
    h.in_transit = h.in_transit - 1 
    db.session.commit()
    return "meow"


@app.route("/api/create", methods=["GET"])
def create_hospital():
    name = request.args.get("name")
    location = request.args.get("location")
    total_beds = request.args.get("total_beds")
    in_transit = request.args.get("in_transit")
    occupied = request.args.get("occupied")

    hospital = Hospital(name=name, location=location, total_beds=total_beds, in_transit=in_transit, occupied=occupied)
    db.session.add(hospital)
    db.session.commit()

    return "meow"