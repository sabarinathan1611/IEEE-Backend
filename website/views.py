from flask import Blueprint, render_template, request, flash, jsonify,redirect, url_for
from flask_login import login_required, current_user
from .auth import send_mail
from .models import Tech_register,Non_register

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
def home():
    return render_template("index.html")


@views.route('/admin',methods=['GET','POST'])
@login_required
def admin():
    if (current_user.admin==True):
        tech=Tech_register.query.order_by(Tech_register.date)
        non_tech=Non_register.query.order_by(Non_register.date)
        print("wrh")
        
    else:
     
        return redirect(url_for('auth.login'))
    return render_template("admin.html",tech=tech,non_tech=non_tech)


@views.route('/tec-register',methods=['GET','POST'])
def tech_register():
        return render_template('register.html')
    

    
@views.route('/non-tec-register',methods=['GET','POST'])
def nontech_register():
        return render_template('nontech_register.html')
    
@views.route('/contact',methods=['POST','GET'])
def connect():
    if request.method=='POST':
        
        name = request.form.get('name')
        number = request.form.get('number')
        mail=request.form.get('mail')
        subject=request.form.get('subject')
        message=request.form.get('message')
        
        email=['vsabarinathan1611@gmail.com','sabarinathan.project@gmail.com']
        body= """Subject:Querry:{} \n\n 
        Name:{},
        Number:{},
        Email:{},
        Message:{},
        """.format(subject,name,number,mail,message)
        send_mail(email, body)
    return redirect(url_for('views.home'))
        