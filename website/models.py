from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class Delete_pass(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    dpassword = db.Column(db.String(150),default="sha256$JgaQQgIqQSPoGuwG$999e51e1640ec65ba78f14593b561d9bcc96b7c28e013966b49b3fb09eabd7dd")



class Event1(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(100))
    email = db.Column(db.String(150))
    rollno=db.Column(db.String(100),unique=True)
    dept=db.Column(db.String(100))
    
    ieee=db.Column(db.String(10))
    # i3emid=db.Column(db.String(10))
    
    event=db.Column(db.String(100))

    teamname=db.Column(db.String(500))
    team_members=db.Column(db.String(500))
    date = db.Column(db.DateTime(timezone=True), default=func.now())

class Event2(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(100))
    email = db.Column(db.String(150))
    rollno=db.Column(db.String(100),unique=True)
    dept=db.Column(db.String(100))
    
    ieee=db.Column(db.String(10))
    # i3emid=db.Column(db.String(10))
    
    event=db.Column(db.String(100))

    teamname=db.Column(db.String(500))
    team_members=db.Column(db.String(500))
    date = db.Column(db.DateTime(timezone=True), default=func.now())

class Event3(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(100))
    email = db.Column(db.String(150))
    rollno=db.Column(db.String(100),unique=True)
    dept=db.Column(db.String(100))
    
    ieee=db.Column(db.String(10))
    # i3emid=db.Column(db.String(10))
    
    event=db.Column(db.String(100))

    teamname=db.Column(db.String(500))
    team_members=db.Column(db.String(500))
    date = db.Column(db.DateTime(timezone=True), default=func.now())

class Event4(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(100))
    email = db.Column(db.String(150))
    rollno=db.Column(db.String(100),unique=True)
    dept=db.Column(db.String(100))
    
    ieee=db.Column(db.String(10))
    # i3emid=db.Column(db.String(10))
    
    event=db.Column(db.String(100))

    teamname=db.Column(db.String(500))
    team_members=db.Column(db.String(500))
    date = db.Column(db.DateTime(timezone=True), default=func.now())

class Event5(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(100))
    email = db.Column(db.String(150))
    rollno=db.Column(db.String(100),unique=True)
    dept=db.Column(db.String(100))
    
    ieee=db.Column(db.String(10))
    # i3emid=db.Column(db.String(10))
    
    event=db.Column(db.String(100))

    teamname=db.Column(db.String(500))
    team_members=db.Column(db.String(500))
    date = db.Column(db.DateTime(timezone=True), default=func.now())

class Event6(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(100))
    email = db.Column(db.String(150))
    rollno=db.Column(db.String(100),unique=True)
    dept=db.Column(db.String(100))
    
    ieee=db.Column(db.String(10))
    # i3emid=db.Column(db.String(10))
    
    event=db.Column(db.String(100))

    teamname=db.Column(db.String(500))
    team_members=db.Column(db.String(500))
    date = db.Column(db.DateTime(timezone=True), default=func.now())

class Event7(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(100))
    email = db.Column(db.String(150))
    rollno=db.Column(db.String(100),unique=True)
    dept=db.Column(db.String(100))
    
    ieee=db.Column(db.String(10))
    # i3emid=db.Column(db.String(10))
    
    event=db.Column(db.String(100))

    teamname=db.Column(db.String(500))
    team_members=db.Column(db.String(500))
    date = db.Column(db.DateTime(timezone=True), default=func.now())

class Event8(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(100))
    email = db.Column(db.String(150))
    rollno=db.Column(db.String(100),unique=True)
    dept=db.Column(db.String(100))
    
    ieee=db.Column(db.String(10))
    # i3emid=db.Column(db.String(10))
    
    event=db.Column(db.String(100))

    teamname=db.Column(db.String(500))
    team_members=db.Column(db.String(500))
    date = db.Column(db.DateTime(timezone=True), default=func.now())

class Event9(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(100))
    email = db.Column(db.String(150))
    rollno=db.Column(db.String(100),unique=True)
    dept=db.Column(db.String(100))
    
    ieee=db.Column(db.String(10))
    # i3emid=db.Column(db.String(10))
    
    event=db.Column(db.String(100))

    teamname=db.Column(db.String(500))
    team_members=db.Column(db.String(500))
    date = db.Column(db.DateTime(timezone=True), default=func.now())

class Screeenshot(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    techevent=db.Column(db.String(100))
    nontechevent=db.Column(db.String(100))
    name=db.Column(db.String(100))
    rollnum=db.Column(db.String(100),unique=True)
    mimetype = db.Column(db.Text, nullable=True)
    img_name = db.Column(db.String(1000), unique=True)
    
    
        
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    admin = db.Column(db.Boolean, default=False)
    username = db.Column(db.String(150),default="admin")
    password = db.Column(db.String(150),default="sha256$d6GCZDY8zefOLAyn$ef4cfa179185989e5f74a2b99d5736bb0362fc166799f5f6fedbe4e22e9109c2")
   
