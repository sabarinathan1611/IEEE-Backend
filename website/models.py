from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class register(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(100))
    email = db.Column(db.String(150), unique=True)
    rollno=db.Column(db.String(100))
    dept=db.Column(db.String(100))
    
    IEEE=db.Column(db.String(10))
    IEEE=db.Column(db.Integer)
    
    event=db.Column(db.String(100))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    admin = db.Column(db.Boolean, default=False)
    username = db.Column(db.String(150))
    password = db.Column(db.String(150))
   
