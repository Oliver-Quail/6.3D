from dataclasses import dataclass

from flask import request, redirect
from flask.json import jsonify

from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import defer

from . import app, db
from .models import Hospital



@app.errorhandler(404)
def not_found(e):
    return app.send_static_file("index.html")

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

    return jsonify(hospital.all())


@app.route("/assign", methods=["POST"])
def assign():

    query = db.select(Hospital.icu_bed, Hospital.in_transit)
    res = db.session.execute(query).one()

    return jsonify(res.all())

    pass
