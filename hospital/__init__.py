import wikipedia
import logging

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, MappedAsDataclass

ARTICLES = [
    "26 Aquilae",
    "Army & Navy Stores (United Kingdom)",
    "Birds Arent Real",
    "Chernobyl disaster",
    "Common ostrich",
    "David Still",
    "DhiTV",
    "Eagle House, London",
    "Gretchen McCord",
    "Isaac I. Moody Jr.",
    "Java",
    "Julianne Kirchner",
    "Lester Bronson",
    "Lucy Burwell Berkeley",
    "Macquarie science reform movement",
    "Money in the Bank (2018)",
    "Mount Hehu",
    "Nathan Peabody Ames",
    "Paleontology in Oklahoma",
    "Passive management",
    "Power Sword",
    "Richard Dodds",
    "Richard Nixon",
    "Ruimsig Stadium",
    "Sick AG",
    "Synthwave",
    "World Bowls",
    "Yellow-throated bush sparrow",
    "Yuri Gagarin",
    "cDVD",
]


app = Flask(__name__, static_folder="../frontend_refactor/dist/", static_url_path="/")
app.logger.setLevel(logging.INFO)


class Base(DeclarativeBase, MappedAsDataclass):
    pass


db = SQLAlchemy(model_class=Base)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///backend.db"
db.init_app(app)

from .models import *

with app.app_context():
    db.create_all()

    for title in ARTICLES:
        query = db.select(Summary).filter_by(title=title)

        if db.session.execute(query).first() is None:
            summary = Summary(
                title=title,
                text=wikipedia.summary(title, auto_suggest=False).replace("\n", " "),
            )
            db.session.add(summary)

    db.session.commit()

from .routes import *