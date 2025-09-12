from . import db

from typing import List
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship


class Hospital(db.Model):
    # No unique but we need a primary key for this ORM to work
    name: Mapped[str] = mapped_column(primary_key=True)
    location :Mapped[str]
    icu_bed :Mapped[int]
    in_transit: Mapped[int]



#class Departments(db.Model):
    