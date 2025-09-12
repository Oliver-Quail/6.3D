from dataclasses import dataclass

from flask import request, redirect
from flask.json import jsonify

from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import defer

from . import app, db
from .models import Hospital




@app.route("/temp", methods=["GET"])
def temp():
    hospital = Hospital(name="Burwood", location="123 street", icu_bed=100, in_transit=90)
    db.session.add(hospital)
    db.session.commit()
    return "aaaa"


@app.route("/hospital", methods=["GET"])
def hospital():
    query = db.select(Hospital)
    hospital = db.session.execute(query).scalars()

    response = jsonify(hospital.all())
    return response


@app.route("/assign", methods=["GET"])
def assign():

    query = db.select(Hospital.icu_bed, Hospital.in_transit)
    res = db.session.execute(query).one()

    max_icu_bed = res.icu_bed
    

    return str(max_icu_bed)

    pass
