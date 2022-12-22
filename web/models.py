from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey, Table, Text

db = SQLAlchemy()


class Team(db.Model):
    __tablename__ = 'teams'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    location = db.Column(db.String(50), nullable=False)
    

class Owner(db.Model):
    __tablename__ = 'owners'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    fullname = db.Column(db.String(50), nullable=False)
    team_id = db.Column(db.Integer, ForeignKey("teams.id"))

