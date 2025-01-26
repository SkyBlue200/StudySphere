from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))

class Physics(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    chapter = db.Column(db.String(150))
    question = db.Column(db.String(150))
    option_1 = db.Column(db.String(150))
    option_2 = db.Column(db.String(150))
    option_3 = db.Column(db.String(150))
    option_4 = db.Column(db.String(150))
    correct_option = db.Column(db.String(150))

class Chemistry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    chapter = db.Column(db.String(150))
    question = db.Column(db.String(150))
    option_1 = db.Column(db.String(150))
    option_2 = db.Column(db.String(150))
    option_3 = db.Column(db.String(150))
    option_4 = db.Column(db.String(150))
    correct_option = db.Column(db.String(150))

class Maths(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    chapter = db.Column(db.String(150))
    question = db.Column(db.String(150))
    option_1 = db.Column(db.String(150))
    option_2 = db.Column(db.String(150))
    option_3 = db.Column(db.String(150))
    option_4 = db.Column(db.String(150))
    correct_option = db.Column(db.String(150))