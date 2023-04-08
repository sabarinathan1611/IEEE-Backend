from flask import Blueprint, render_template, request, flash, jsonify, redirect, url_for, current_app, make_response
from flask_login import login_required, current_user
from werkzeug.security import check_password_hash
from .auth import send_mail
from .models import Event1, Event2, Event3, Event4, Event5, Event6, Event7, Event8, Event9, Delete_pass, Screeenshot
from . import db
from werkzeug.utils import secure_filename  # for secure file
from random import randint
import uuid
import os
from website import create_app
import json

views = Blueprint('views', __name__)
# Allowed Extensions
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'webp', 'raw', 'svg'])

app = create_app()


def allowed_file(filename):
    return '.' in filename and filename.rsplit(
        '.', 1)[1].lower() in ALLOWED_EXTENSIONS


@views.route('/', methods=['GET', 'POST'])
def home():
    return render_template("index.html")


@views.route('/admin', methods=['GET', 'POST'])
@login_required
def admin():
    if (current_user.admin == True):
        event1 = Event1.query.order_by(Event1.date)
        event2 = Event2.query.order_by(Event2.date)
        event3 = Event3.query.order_by(Event3.date)
        event4 = Event4.query.order_by(Event4.date)
        event5 = Event5.query.order_by(Event5.date)
        event6 = Event6.query.order_by(Event6.date)
        event7 = Event7.query.order_by(Event7.date)
        event8 = Event8.query.order_by(Event8.date)
        event9 = Event9.query.order_by(Event9.date)

    else:

        return redirect(url_for('auth.login'))
    return render_template("admin.html", event1=event1, event2=event2, event3=event3, event4=event4, event5=event5, event6=event6, event7=event7, event8=event8, event9=event9)


@views.route('/register', methods=['GET', 'POST'])
def register():
    return render_template('register.html')


@views.route('/contact', methods=['POST', 'GET'])
def connect():
    if request.method == 'POST':

        name = request.form.get('name')
        number = request.form.get('number')
        mail = request.form.get('mail')
        subject = request.form.get('subject')
        message = request.form.get('message')

        email = ['2021pecit233@gmail.com',
                 'sabarinathan.project@gmail.com']
        body = """Subject:Querry:{} \n\n 
        Name:{},
        Number:{},
        Email:{},
        Message:{},
        """.format(subject, name, number, mail, message)
        send_mail(email, body)
    return redirect(url_for('views.home'))


@views.route('/delete-data', methods=['POST', 'GET'])
@login_required
def delete():

    if request.method == 'POST':

        password = request.form.get('pass')

        deletepassword = Delete_pass.query.filter_by(id=1).first()
        print(deletepassword, password)
        if deletepassword:
            if check_password_hash(deletepassword.dpassword, password):        
                event1 = Event1.query.order_by(Event1.date)
                event2 = Event2.query.order_by(Event2.date)
                event3 = Event3.query.order_by(Event3.date)
                event4 = Event4.query.order_by(Event4.date)
                event5 = Event5.query.order_by(Event5.date)
                event6 = Event6.query.order_by(Event6.date)
                event7 = Event7.query.order_by(Event7.date)
                event8 = Event8.query.order_by(Event8.date)
                event9 = Event9.query.order_by(Event9.date)
                #Table 1
                for e1 in event1 :
                    event1_data = Event1.query.get(e1.id)
                    db.session.delete(event1_data)
                    db.session.commit()
                 #Table 2
                for e2 in event2 :
                    event2_data = Event2.query.get(e2.id)
                    db.session.delete(event2_data)
                    db.session.commit()
                 #Table 3 
                for e3 in event3 :
                    event3_data = Event3.query.get(e3.id)
                    db.session.delete(event3_data)
                    db.session.commit()
                 #Table 4
                 
                for e4 in event4 :
                    event4_data = Event4.query.get(e4.id)
                    db.session.delete(event4_data)
                    db.session.commit()
                 #Table 5
                for e5 in event5 :
                    event5_data = Event5.query.get(e5.id)
                    db.session.delete(event5_data)
                    db.session.commit()
                 #Table 6
                for e6 in event6 :
                    event6_data = Event6.query.get(e6.id)
                    db.session.delete(event6_data)
                    db.session.commit()
                 #Table 7
                for e7 in event7 :
                    event7_data = Event7.query.get(e7.id)
                    db.session.delete(event7_data)
                    db.session.commit()
                #Table 8
                for e8 in event8 :
                    event8_data = Event8.query.get(e8.id)
                    db.session.delete(event8_data)
                    db.session.commit()
                #Table 9
                for e9 in event9 :
                    event9_data = Event9.query.get(e9.id)
                    db.session.delete(event9_data)
                    db.session.commit()
                
            else:
                flash("Wrong Password")
        else:
            new = Delete_pass()
            db.session.add(new)
            db.session.commit()

    return redirect(url_for('views.admin'))


@views.route('/delete-photo',methods=['POST','GET'])
def delet_photo():
    if request.method == 'POST':
            
        photo = json.loads(request.data)
        img_id = photo['imageID']
        image=Screeenshot.query.get(img_id)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], image.img_name)
        db.session.delete(image)
        db.session.commit()
        os.remove(filepath)      
    return redirect(url_for('views.upload_photo'))

@views.route('/pic-verify', methods=['POST', 'GET'])
@login_required
def upload_photo():
    photos = Screeenshot.query.order_by(Screeenshot.id)
    return render_template('verify.html', photos=photos)