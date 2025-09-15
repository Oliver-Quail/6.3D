import logging

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, MappedAsDataclass
from flask_cors import CORS, cross_origin

app = Flask(__name__)
app.logger.setLevel(logging.INFO)
cors = CORS(app)

class Base(DeclarativeBase, MappedAsDataclass):
    pass

db = SQLAlchemy(model_class=Base)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///backend.db"
db.init_app(app)

from .models import *

with app.app_context():
    db.create_all()



from .routes import *