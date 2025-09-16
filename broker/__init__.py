import logging

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, MappedAsDataclass
from flask_cors import CORS, cross_origin
from apscheduler.schedulers.background import BackgroundScheduler
app = Flask(__name__)
app.logger.setLevel(logging.INFO)
cors = CORS(app)

class Base(DeclarativeBase, MappedAsDataclass):
    pass

db = SQLAlchemy(model_class=Base)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///broker.db"
db.init_app(app)

from .models import *

with app.app_context():
    db.create_all()



def update_service():
    import requests

    print("Running service")



scheduler = BackgroundScheduler()
job = scheduler.add_job(update_service, "interval", minutes=1)


from .routes import *