from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User, Event1, Event2, Event3, Event4, Event5, Event6, Event7, Event8, Event9, Screeenshot
from werkzeug.security import generate_password_hash, check_password_hash
from . import db  # means from __init__.py import db
from .registerget import nontechget, techget
import smtplib
from flask_login import login_user, login_required, logout_user, current_user
from website import create_app
import os
from werkzeug.utils import secure_filename  # for secure file
import uuid

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'webp', 'raw', 'svg'])

app = 'create_app()'


def allowed_file(filename):
    return '.' in filename and filename.rsplit(
        '.', 1)[1].lower() in ALLOWED_EXTENSIONS


def create_admin():
    print("password:", generate_password_hash("onepiece", method='sha256'))
    user = User.query.filter_by(id=1).first()
    if not user:
        new_user = User(admin=True)
        db.session.add(new_user)
        db.session.commit()
        print('Created Admin!')


def send_mail(email, body):
    sender_email = "ieeeeventit@gmail.com"
    receiver_email = email
    password = "hbsapqyrcvcdjqjl"
    message = body
    print("wefdwefugyuhg")

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)
    print('*****Email sent!*****')
    server.quit()


auth = Blueprint('auth', __name__)
app = create_app()


def photoupload(pic, techevent,nontechevent, name, rollno):

                    try:
                        # check if request contains files and image attribute exists
                        if 'image' not in request.files:
                            raise FileNotFoundError('No image uploaded')

                        # validate mimetype of uploaded image
                        if not pic.mimetype.startswith('image/'):
                            raise TypeError('Invalid file type')

                        # validate if the file has allowed extensions
                        if not allowed_file(pic.filename):
                            raise ValueError(
                                "Allowed file extensions: 'png', 'jpg', 'jpeg', 'webp', 'raw', 'svg'")
                        if not os.path.exists(app.config['UPLOAD_FOLDER']):
                            flash("oombu")
                        filename = secure_filename(pic.filename)

                        pic_name = str(uuid.uuid1()) + '_' + filename

                        filepath = os.path.join(
                            app.config['UPLOAD_FOLDER'], pic_name)

                        

                        upload = Screeenshot(techevent=techevent,nontechevent=nontechevent, name=name, rollnum=rollno, img_name=pic_name)
                        db.session.add(upload)
                        db.session.commit()
                        pic.save(filepath)

                        flash('File uploaded successfully.')

                        return redirect('/')

                    except (TypeError, ValueError, KeyError, FileNotFoundError) as e:
                            print("Error varuthu ")
                            flash(str(e))

# register


@auth.route('/registerdb', methods=['GET', 'POST'])
def registerdb():
    if request.method == "POST":
        name = request.form.get('name')
        pic = request.files['image']

        rollno = request.form.get('rollno')

        dept = request.form.get('dept')

        ieee = request.form.get('ieee')

        i3emid = request.form.get('memberid')

        email = request.form.get('email')

        tech_teamname = request.form.get('teamname1')

        tech_memember = request.form.get('team-members1')

        nontech_teamname = request.form.get('teamname2')
        nontech_memember = request.form.get('team-members2')

        if dept == 'no':
            flash("ADD DEPT")
            return redirect(url_for('views.tech_register'))

        techis = request.form.get('techval')
        print(techis)
        nontechis = request.form.get('nontechval')

        event1 = request.form.get('event1')
        event2 = request.form.get('event2')
        event3 = request.form.get('event3')
        event4 = request.form.get('event4')
        event5 = request.form.get('event5')
        event6 = request.form.get('event6')
        event7 = request.form.get('event7')
        event8 = request.form.get('event8')
        event9 = request.form.get('event9')
        # print("EVENT5:",event5)
        # print("NONtech type:",teamName)

        result = techget(name=name, dept=dept, ieee=ieee, i3emid=i3emid, email=email, tech_teamname=tech_teamname, tech_memember=tech_memember,
                         techis=techis, event1=event1, event2=event2, event3=event3, event4=event4, event5=event5, rollno=rollno)
        nontech_result = nontechget(name=name, dept=dept, ieee=ieee, i3emid=i3emid, email=email, nontech_teamname=nontech_teamname,
                                    nontech_memember=nontech_memember, nontechis=nontechis, event6=event6, event7=event7, event8=event8, event9=event9, rollno=rollno)
        final= """"
        Tech Event: {} \n\n
        NonTech EVent: {}
                """.format(result,nontech_result)
       
        if ieee == 'yes':
                    photoupload(pic=pic,techevent=result,nontechevent=nontech_result , name=name, rollno=rollno)

                    

              
      

        message = """Subject:Welcome to the IEEE Event \n\n
                    Welcome and thank you for registering for the IEEE Event {},{}. We're looking forward to an exciting and informative event.
                
                    We hope to provide you with resources and information to further your knowledge and interests in the field of IEEE.
                
                    Do not hesitate to reach out to us if you have any questions along the way!
                
                    Sincerely,
                    The IEEE Team""".format(result, nontech_result)
        # send_mail( email= email,body=message)
        print("Message: ", message)

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
