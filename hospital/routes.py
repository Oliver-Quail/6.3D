import random
import os

from typing import List
from dataclasses import dataclass

from flask import request, redirect
from flask.json import jsonify

from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import defer

from . import app, db
from .models import Team, Algorithm, Plaintext, Code, Summary, Cracked
from .tester import (
    test_algorithm,
    EncrypterEvalError,
    DecrypterEvalError,
    DecryptionError,
    InvalidAlgorithmError
)


@app.errorhandler(404)
def not_found(e):
    return app.send_static_file("index.html")


@app.route("/api/teams", methods=["GET", "POST"])
def teams():
    if request.method == "POST":
        # Create a new team, returning the team id
        team = Team(name=request.data.decode())

        try:
            db.session.add(team)
            db.session.commit()
            app.logger.info(f"Created team {team.name}")
        except IntegrityError:
            app.logger.warning(f"Tried to create already existing team {team.name}")
            return "Failed to create team. Team name already exists", 403

        return jsonify(team)

    elif request.method == "GET":
        # Get a list of existing teams
        query = db.select(Team)
        teams = db.session.execute(query).scalars()
        return jsonify(teams.all())


@app.route("/api/algorithms", methods=["GET", "POST"])
def algorithms():
    if request.method == "POST":
        # Create a new algorithm, returning the algorithm
        # id

        data = request.json
        encrypter = data["encrypter"]
        decrypter = data["decrypter"]
        team_id = data["team_id"]

        query = db.select(Team).filter_by(id=team_id)
        team = db.session.execute(query).scalar_one_or_none()

        if team is None:
            return "Unknown team ID", 403

        query = db.select(Summary)
        summaries = db.session.execute(query).scalars()
        summary = random.choice(summaries.all())
        plaintext = summary.text

        cyphertext = None

        app.logger.info("New algorithm upload")
        app.logger.info(f"Encrypter:\n {encrypter}")
        app.logger.info(f"Decrypter:\n {decrypter}")

        try:
            cyphertext = test_algorithm(encrypter, decrypter, plaintext)
        except EncrypterEvalError as e:
            app.logger.warning(f"Failed to eval encrypter: {e}")
            return str(e), 400
        except DecrypterEvalError as e:
            app.logger.warning(f"Failed to eval decrypter: {e}")
            return str(e), 400
        except DecryptionError as e:
            app.logger.warning(f"Failed to eval decrypter: {e}")
            return str(e), 400
        except InvalidAlgorithmError as e:
            return str(e), 403

        if cyphertext is None:
            # scripts were parsed and ran however it did not successfully
            # encrypt then decyrpt the plaintext
            app.logger.warning(
                "Encryption then decryption of the plaintext did not return the same result"
            )
            return (
                "Encryption then decryption of a plaintext did not return the same result",
                400,
            )

        algorithm = Algorithm(
            team_id=team.id,
            cyphertext=cyphertext,
        )

        db.session.add(algorithm)
        db.session.commit()

        plaintext = Plaintext(
            algorithm_id=algorithm.id,
            summary_id=summary.id,
        )

        code = Code(
            algorithm_id=algorithm.id,
            encrypter=encrypter,
            decrypter=decrypter,
        )

        db.session.add(plaintext)
        db.session.add(code)
        db.session.commit()

        return jsonify(algorithm)

    elif request.method == "GET":
        # Get a list of existing algorithms
        query = db.select(Algorithm)
        algorithms = db.session.execute(query).scalars()

        return jsonify(algorithms.all())


@app.route("/api/algorithms/solve/<algorithm_id>", methods=["POST"])
def solve(algorithm_id):
    team_id = request.json["team_id"]

    query = db.select(Team).filter_by(id=team_id)
    team = db.session.execute(query).scalar_one_or_none()

    if team is None:
        return "Unknown team ID", 403

    for solved in team.solved:
        if solved.id == algorithm_id:
            return "You have already solved this algorithm", 403

    query = db.select(Algorithm).filter_by(id=algorithm_id)
    algorithm = db.one_or_404(query)

    if algorithm.team_id == team_id:
        return "Solving your own algorithm kinda defeats the purpose", 403

    query = db.select(Plaintext).filter_by(algorithm_id=algorithm.id)
    plaintext = db.session.execute(query).scalar_one()

    if request.json["text"].strip() == plaintext.summary.text:
        solve = Cracked(team_id, algorithm.id)

        try:
            db.session.add(solve)
            db.session.commit()
        except IntegrityError:
            return "Your team has already solved this algorithm", 400

        app.logger.info(f"{team.name} cracked {algorithm.id}")
        return "Success", 200

    app.logger.info(f"{team.name} failed to crack {algorithm.id}")
    return "Incorrect plain text", 400