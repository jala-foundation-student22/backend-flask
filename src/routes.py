from flask import jsonify, make_response, request
from sqlalchemy import select
from src.models import Task
from src import app, db


@app.route("/task/", methods=["GET"])
def get_all_tasks():
    try:
        with db.session():
            tasks = db.session.query(Task).all()
            return make_response(jsonify({"tasks": [task.json() for task in tasks]}))
    except Exception as e:
        return make_response(
            jsonify({"message": "Couldn't get tasks. Error: %s" % (e)}), 500
        )


@app.route("/task/<int:id>/", methods=["GET"])
def get_task(id):
    try:
        with db.session():
            task = db.session.query(Task).filter(id == id).first()
            return make_response(jsonify(task.json()))
    except Exception as e:
        return make_response(
            jsonify({"message": "Couldn't get task. Error: %s" % (e)}), 500
        )


@app.route("/task/", methods=["POST"])
def create_task():
    try:
        data = request.json
        task = Task(
            name=data["name"],
            description=data["description"],
            category=data["category"],
            deadline=data["deadline"],
            status=data["status"],
        )
        with db.session():
            db.session.add(task)
            db.session.commit()
        return make_response(
            jsonify({"message": "task %s created successfully" % (task.name)}), 201
        )
    except Exception as e:
        return make_response(
            jsonify({"message": "Couldn't create task. Error: %s" % (e)}), 500
        )
