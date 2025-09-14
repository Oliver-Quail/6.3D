from dataclasses import dataclass

from flask import request, redirect
from flask.json import jsonify

from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import defer

from . import app, db
from .models import Hospital

@app.route("/init", methods=["GET"])
def temp():
    hospital = Hospital(name="Burwood", location="123 street", total_beds=100, in_transit=40, occupied=30)
    db.session.add(hospital)
    db.session.commit()
    return "meow"


@app.route("/hospital", methods=["GET"])
def hospital():
    query = db.select(Hospital)
    hospital = db.session.execute(query).scalars()

    response = jsonify(hospital.all())
    return response


@app.route("/assign", methods=["GET"])
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


@app.route("/deassign", methods=["GET"])
def deassign():
    h = db.session.query(Hospital).first()
    h.in_transit = h.in_transit - 1 
    db.session.commit()
    return "meow"
