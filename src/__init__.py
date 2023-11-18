import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


absolute_path = os.path.dirname(__file__)
app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(
    absolute_path, "todo.db"
)
app.config["SECRET_KEY"] = "a1b2c3d4"

db = SQLAlchemy(app)

from src import models, routes
