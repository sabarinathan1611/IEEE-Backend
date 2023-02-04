from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class Tech_register(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(100))
    email = db.Column(db.String(150))
    rollno=db.Column(db.String(100))
    dept=db.Column(db.String(100))
    
    ieee=db.Column(db.String(10))
    i3emid= db.Column(db.String(100))
    
    event=db.Column(db.String(100))
    teamname=db.Column(db.String(500))
    team_members=db.Column(db.String(500))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    

class Non_register (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(100))
    email = db.Column(db.String(150))
    rollno=db.Column(db.String(100))
    dept=db.Column(db.String(100))
    
    ieee=db.Column(db.String(10))
    i3emid=db.Column(db.String(10))
    
    event=db.Column(db.String(100))
    teamname=db.Column(db.String(500))
    team_members=db.Column(db.String(500))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    admin = db.Column(db.Boolean, default=False)
    username = db.Column(db.String(150))
    password = db.Column(db.String(150))
   
