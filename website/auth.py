from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User,Tech_register,Non_register
from werkzeug.security import generate_password_hash, check_password_hash
from . import db   ##means from __init__.py import db
import smtplib
from flask_login import login_user, login_required, logout_user, current_user

def create_admin():
            print("password:",generate_password_hash("onepiece", method='sha256'))
            user=User.query.filter_by(id=1).first()
            if not user:
                new_user = User(admin=True)
                db.session.add(new_user)
                db.session.commit()
                print('Created Admin!')
                

def send_mail(email,body):
    sender_email = "ieee.event2023@gmail.com"
    receiver_email = email
    password = "btugxzcfwugzxuhu"
    message =body
    print("wefdwefugyuhg")
    
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)
    print('*****Email sent!*****')
    server.quit()


auth = Blueprint('auth', __name__)
#tech register
@auth.route('/registerdb',methods=['GET','POST'])
def registerdb():
    if request.method=="POST":
        result=' '
        nontech_result=' '
        name =request.form.get('name')
        
        rollno=request.form.get('rollno')
        
        dept=request.form.get('dept')
        
        ieee=request.form.get('ieee')
        
        i3emid=request.form.get('memberid')
        
        email =request.form.get('email')
        
        
        
        teamName=request.form.get('teamName')
        
        team_members=request.form.get('team-members')
        
        techis=request.form.get('techval')
        nontechis=request.form.get('nontechval')
  
        event1=request.form.get('event1')
        event2=request.form.get('event2')
        event3=request.form.get('event3')
        event4=request.form.get('event4')
        event5=request.form.get('event5')
        event6=request.form.get('event6')
        event7=request.form.get('event7')
        event8=request.form.get('event8')
        #print("EVENT5:",event5)
        print("NONtech type:",event5)
        
        a=[]   
           
        if techis== '1':
            if event1 == 'on':
                a.append('WIKIPEDIA SPEEDRUN')
                
            if event2 == 'on':
                a.append('CODE COMBACKT')
                
            if event3 == 'on':
                a.append('HACK CRACK')
                
            if event4 == 'on':
                
                a.append('EXPRESS ON')     
                    
            roll=Tech_register.query.filter_by(rollno=rollno).first()

            if roll is None :
                my_list = a
                result = ','.join(my_list)
                #print("TECH Result::",result)

                
                new_reg=Tech_register(name=name,rollno=rollno,dept=dept,ieee=ieee,i3emid=i3emid,email=email,event=result,teamname=teamName,team_members=team_members)
                db.session.add(new_reg)
                db.session.commit()
                a.clear()

                
            else:
                flash("You already registered for this event")
                
        b=[]    
        if nontechis =='1':            
            
            if event5 == 'on':
                a.append('GEOGUESSER')
                
            if event6 == 'on':
               a.append('LIGHT CAMERA ACTION')
                
            if event7 == 'on':
               a.append('SHIP WRECK')
                
            if event8 == 'on':
                
               a.append('60 SECONDS FAME')  
            roll=Non_register.query.filter_by(rollno=rollno).first()
       
            if roll is None:
                nontech_list = a
                nontech_result = ','.join(nontech_list)
                print("NON TECH::",nontech_result)
                
                new_reg=Non_register(name=name,rollno=rollno,dept=dept,ieee=ieee,i3emid=i3emid,email=email,event=nontech_result,teamname=teamName,team_members=team_members)
                db.session.add(new_reg)
                db.session.commit() 
                a.clear()  
                print("TECH RESULT:",result,'\n\n','NONTECH',nontech_result)
            else:
                flash("You already registered for this event")
                return redirect(url_for('views.tech_register'))
            
            
        message="""Subject:Welcome to the IEEE Event \n\n
    Welcome and thank you for registering for the IEEE Event {} {}. We're looking forward to an exciting and informative event.

    We hope to provide you with resources and information to further your knowledge and interests in the field of IEEE.

    Do not hesitate to reach out to us if you have any questions along the way!

    Sincerely,
    The IEEE Team""".format(result,nontech_result)
        send_mail( email= email,body=message)
      
      
    return redirect(url_for('views.home'))


@auth.route('/login', methods=['GET', 'POST'])
def login():
    
    if request.method == 'POST':
        userName = request.form.get('username')
        password = request.form.get('pass')


        user = User.query.filter_by(id=1).first()
        print(user.username)
        
        if user.username == userName:
            
            
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                print("111")
                
                return redirect(url_for('views.admin'))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
                # passs="admin"
                # new_user = User(username="admin",password=generate_password_hash(passs, method='sha256'),admin=True)
                # db.session.add(new_user)
                # db.session.commit()
                flash('Username does not exist.', category='error')


    return render_template("login.html", user=current_user)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    
    return redirect(url_for('views.home'))

@auth.route('/create-admin', methods=['GET', 'POST'])
def newadmin():
    create_admin()
    return redirect(url_for('auth.login')) 

