from datetime import datetime
from config import db

class User(db.Model):
    __tablename__ = "Users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    creation_date = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

class Link(db.Model):
    __tablename__ = "Links"
    id = db.Column(db.Integer, primary_key=True)
    short_Url = db.Column(db.String(7), nullable=False)
    original_Url = db.Column(db.String, nullable=False)
    user_id = db.Column(db.Integer, nullable=False)
    creation_date = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
