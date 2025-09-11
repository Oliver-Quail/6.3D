from . import db

from typing import List
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship


class Team(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, init=False)
    name: Mapped[str] = mapped_column(unique=True)

    algorithms: Mapped[List["Algorithm"]] = relationship(init=False)
    solved: Mapped[List["Algorithm"]] = relationship(secondary="cracked", init=False)


class Code(db.Model):
    """A table specifically for admin tasks"""

    id: Mapped[int] = mapped_column(primary_key=True, init=False)
    algorithm_id: Mapped[int] = mapped_column(ForeignKey("algorithm.id"))

    encrypter: Mapped[str]
    decrypter: Mapped[str]


class Summary(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, init=False)
    title: Mapped[str]
    text: Mapped[str]


class Plaintext(db.Model):
    algorithm_id: Mapped[int] = mapped_column(
        ForeignKey("algorithm.id"), primary_key=True
    )
    summary_id: Mapped[int] = mapped_column(ForeignKey("summary.id"), primary_key=True)
    summary = relationship("Summary")


class Algorithm(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, init=False)
    team_id: Mapped[int] = mapped_column(ForeignKey("team.id"))
    cyphertext: Mapped[str]


class Cracked(db.Model):
    team_id: Mapped[int] = mapped_column(ForeignKey("team.id"), primary_key=True)
    algorithm_id: Mapped[int] = mapped_column(
        ForeignKey("algorithm.id"), primary_key=True
    )