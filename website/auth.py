from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User,Tech_register,Non_register
from werkzeug.security import generate_password_hash, check_password_hash
from . import db   ##means from __init__.py import db
from flask_login import login_user, login_required, logout_user, current_user


auth = Blueprint('auth', __name__)
#tech register
@auth.route('/registerdb',methods=['GET','POST'])
def registerdb():
    if request.method=="POST":
        name =request.form.get('name')
        
        rollno=request.form.get('rollno')
        
        dept=request.form.get('dept')
        
        ieee=request.form.get('ieee')
        
        i3emid=request.form.get('memberid')
        
        email =request.form.get('email')
        
        event= request.form.get('event')
        
        teamName=request.form.get('teamName')
        
        team_members=request.form.get('team-members')
        new_reg=Tech_register(name=name,rollno=rollno,dept=dept,ieee=ieee,i3emid=i3emid,email=email,event=event,teamname=teamName,team_members=team_members)
        db.session.add(new_reg)
        db.session.commit()
        print("1.name:",name,'\n',"2.rollno",rollno,'\n',"3.dept",dept,'\n',"4.ieee",ieee,'\n',"5.i3emid",i3emid,'\n',"6.email",email,'/n',"7.event",event,'\n',"8.team_members",team_members,'\n',"9.teamName",teamName)
    return redirect(url_for('views.home'))
#non tech register
@auth.route('/registerdb1',methods=['GET','POST'])
def registerdb1():
    if request.method=="POST":
        name =request.form.get('name')
        
        rollno=request.form.get('rollno')
        
        dept=request.form.get('dept')
        
        ieee=request.form.get('ieee')
        
        i3emid=request.form.get('memberid')
        
        email =request.form.get('email')
        
        event= request.form.get('event')
        
        teamName=request.form.get('teamName')
        
        team_members=request.form.get('team-members')
        new_reg=Non_register(name=name,rollno=rollno,dept=dept,ieee=ieee,i3emid=i3emid,email=email,event=event,teamname=teamName,team_members=team_members)
        db.session.add(new_reg)
        db.session.commit()
        print("1.name:",name,'\n',"2.rollno",rollno,'\n',"3.dept",dept,'\n',"4.ieee",ieee,'\n',"5.i3emid",i3emid,'\n',"6.email",email,'/n',"7.event",event,'\n',"8.team_members",team_members,'\n',"9.teamName",teamName)
    return redirect(url_for('views.home'))

@auth.route('/login', methods=['GET', 'POST'])
def login():
    
    if request.method == 'POST':
        userName = request.form.get('username')
        password = request.form.get('pass')
        # new_user = User(username=userName,password=generate_password_hash(password, method='sha256'),admin=True)
        # db.session.add(new_user)
        # db.session.commit()
    
        user = User.query.filter_by(username=userName).first()
        
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                print("111")
                return redirect(url_for('views.admin'))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Email does not exist.', category='error')

    return render_template("login.html", user=current_user)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

