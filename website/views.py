from flask import Blueprint, render_template, request, flash, jsonify, redirect, url_for,current_app, make_response
from flask_login import login_required, current_user
from werkzeug.security import check_password_hash
from .auth import send_mail
from .models import Tech_register, Non_register,Delete_pass
from . import db
from werkzeug.utils import secure_filename  #for secure file
from random import randint
import uuid
import os
from website import create_app
views = Blueprint('views', __name__)
#Allowed Extensions
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'webp','raw','svg'])

app=create_app()

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
        tech = Tech_register.query.order_by(Tech_register.date)
        non_tech = Non_register.query.order_by(Non_register.date)
        

    else:

        return redirect(url_for('auth.login'))
    return render_template("admin.html", tech=tech, non_tech=non_tech)


@views.route('/register', methods=['GET', 'POST'])
def tech_register():
    return render_template('register.html')



@views.route('/contact', methods=['POST', 'GET'])
def connect():
    if request.method == 'POST':

        name = request.form.get('name')
        number = request.form.get('number')
        mail = request.form.get('mail')
        subject = request.form.get('subject')
        message = request.form.get('message')

        email = ['vsabarinathan1611@gmail.com',
                 'sabarinathan.project@gmail.com']
        body = """Subject:Querry:{} \n\n 
        Name:{},
        Number:{},
        Email:{},
        Message:{},
        """.format(subject, name, number, mail, message)
        send_mail(email, body)
    return redirect(url_for('views.home'))


@views.route('/delete-data',methods=['POST','GET'])
@login_required
def delete():
    
    if request.method=='POST':
      
        password=request.form.get('pass')
        
        deletepassword= Delete_pass.query.filter_by(id=1).first()
        print(deletepassword,password)
        if deletepassword:
                if check_password_hash(deletepassword.dpassword, password):
                        tech = Tech_register.query.order_by(Tech_register.date)
                        non_tech = Non_register.query.order_by(Non_register.date)
                        for t in tech:
                            tech_data=Tech_register.query.get(t.id)
                            db.session.delete(tech_data)
                            db.session.commit()
                        for n in non_tech:
                            nontech_data=Non_register.query.get(n.id)
                            db.session.delete(nontech_data)
                            db.session.commit()
                else:
                        flash("Wrong Password")
        else:
            new = Delete_pass()
            db.session.add(new)
            db.session.commit()
            
    return redirect(url_for('views.admin'))


@views.route('/upload', methods=['POST','GET'])
def upload_photo():
    if request.method=='POST':
            
        try:
            # check if request contains files and image attribute exists
            if 'image' not in request.files:
                raise FileNotFoundError('No image uploaded')
            
            pic = request.files['image']

            # validate mimetype of uploaded image
            if not pic.mimetype.startswith('image/'):
                raise TypeError('Invalid file type')

            # validate if the file has allowed extensions
            if not allowed_file(pic.filename):
                raise ValueError("Allowed file extensions: 'png', 'jpg', 'jpeg', 'webp', 'raw', 'svg'")
            if not os.path.exists(app.config['UPLOAD_FOLDER']):
                flash("oombu")
            filename = secure_filename(pic.filename)

            pic_name = str(uuid.uuid1()) + '_' + filename
            
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], pic_name)
            
            pic.save(filepath)
            
            flash('File uploaded successfully.')
            
            return redirect('/')
        
        except (TypeError, ValueError, KeyError, FileNotFoundError) as e:
            flash(str(e))

    return render_template('upload.html')