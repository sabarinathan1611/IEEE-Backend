from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User, Event1, Event2, Event3, Event4, Event5, Event6, Event7, Event8, Event9, Screeenshot
from werkzeug.security import generate_password_hash, check_password_hash
from . import db  # means from __init__.py import db

import smtplib
from flask_login import login_user, login_required, logout_user, current_user
from website import create_app
import os
from werkzeug.utils import secure_filename  # for secure file
import uuid

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'webp', 'raw', 'svg', 'pdf'])

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

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)
    print('*****Email sent!*****')
    server.quit()


auth = Blueprint('auth', __name__)
app = create_app()


def photoupload(pic, techevent, nontechevent, name, rollno):

    try:
        # check if request contains files and image attribute exists
        if 'image' not in request.files:
            raise FileNotFoundError('No image uploaded')

        # validate mimetype of uploaded image
        # if not pic.mimetype.startswith('image/'):
        #     raise TypeError('Invalid file type')

        # validate if the file has allowed extensions
        if not allowed_file(pic.filename):
            raise ValueError(
                "Allowed file extensions: 'png', 'jpg', 'jpeg', 'webp', 'raw', 'svg'")

        if not os.path.exists(app.config['UPLOAD_FOLDER']):
            flash("Path Not Found")

        filename = secure_filename(pic.filename)

        pic_name = str(uuid.uuid1()) + '_' + filename

        filepath = os.path.join(
            app.config['UPLOAD_FOLDER'], pic_name)

        mimetype = pic.mimetype

        upload = Screeenshot(techevent=techevent, nontechevent=nontechevent,
                             name=name, rollnum=rollno, img_name=pic_name, mimetype=mimetype)
        db.session.add(upload)
        db.session.commit()
        pic.save(filepath)

        return True

    except (TypeError, ValueError, KeyError, FileNotFoundError) as e:
        print("Error varuthu ")
        flash(str(e))
        return redirect(url_for('views.register'))

# register


@auth.route('/registerdb', methods=['GET', 'POST'])
def registerdb():
    error = 0

    if request.method == "POST":
                nontech_result = ' '
                result = ' '

                name = request.form.get('name')
                pic = request.files['image']

                rollno = request.form.get('rollno')

                dept = request.form.get('dept')

                ieee = request.form.get('ieee')

                year = request.form.get('year')

                email = request.form.get('email')

                teamname = request.form.get('teammember')

                memember = request.form.get('teammember')

                techis = request.form.get('techval')
                
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

                print("Name:", name, "\n", "Pic:", pic, "\n", "Rollno:", rollno, "\n",
                    "Dept:", dept, "\n", "Year:", year, "\n", "Email:", email, "\n","EVENRT8:",nontechis)

                roll1 = Event1.query.filter_by(rollno=rollno).first()
                roll2 = Event2.query.filter_by(rollno=rollno).first()
                roll3 = Event3.query.filter_by(rollno=rollno).first()
                roll4 = Event4.query.filter_by(rollno=rollno).first()
                roll5 = Event5.query.filter_by(rollno=rollno).first()
                roll6 = Event6.query.filter_by(rollno=rollno).first()
                roll7 = Event7.query.filter_by(rollno=rollno).first()
                roll8 = Event1.query.filter_by(rollno=rollno).first()
                roll9 = Event9.query.filter_by(rollno=rollno).first()

                a = []
                if techis == '1':
                    if event1 == 'on':
                        if roll1:
                            flash("You already register for this event")
                            return render_template('register.html')
                        elif roll1 is None:
                            a.append('Event 1')
                            my_list = a
                            result = ','.join(my_list)
                            # print("TECH Result::",result)
                            new_reg = Event1(name=name, rollno=rollno, dept=dept, ieee=ieee, event='event1', year=year,
                                            email=email, teamname=teamname, team_members=teamname)
                            db.session.add(new_reg)
                            db.session.commit()

                    if event2 == 'on':
                        if roll2:
                            flash("You already register for this event")
                            return render_template('register.html')
                        elif roll2 is None:
                            a.append('Event 2')
                            my_list = a
                            result = ','.join(my_list)
                            # print("TECH Result::",result)
                            new_reg = Event2(name=name, rollno=rollno, dept=dept, ieee=ieee, event='event2', year=year,
                                            email=email, teamname=teamname, team_members=memember)
                            db.session.add(new_reg)
                            db.session.commit()

                    if event3 == 'on':
                        if roll3:
                            flash("You already register for this event")
                            return render_template('register.html')
                        elif roll3 is None:
                            a.append('Event 3')
                            my_list = a
                            result = ','.join(my_list)
                            # print("TECH Result::",result)
                            new_reg = Event3(name=name, rollno=rollno, dept=dept, ieee=ieee, event='event3', year=year,
                                            email=email, teamname=teamname, team_members=memember)
                            db.session.add(new_reg)
                            db.session.commit()

                    if event4 == 'on':
                        if roll4:
                            flash("You already register for this event")
                            return render_template('register.html')
                        elif roll4 is None:
                            a.append('Event 4')
                            my_list = a
                            result = ','.join(my_list)
                            # print("TECH Result::",result)
                            new_reg = Event4(name=name, rollno=rollno, dept=dept, ieee=ieee, event='event4', year=year,
                                            email=email, teamname=teamname, team_members=memember)
                            db.session.add(new_reg)
                            db.session.commit()

                        a.append('DESTINATION JUNCTION')
                    if event5 == 'on':
                        if roll5:
                            flash("You already register for this event")
                            return render_template('register.html')
                        a.append('Event 5')

                        limit = Event5.query.filter_by(id=20).first()
                        if limit:
                            flash("Team event is full")
                        if roll5 is None:
                            my_list = a
                            result = ','.join(my_list)
                            # print("TECH Result::",result)
                            new_reg = Event5(name=name, rollno=rollno, dept=dept, ieee=ieee, event='event5', year=year,
                                            email=email, teamname=teamname, team_members=memember)
                            db.session.add(new_reg)
                            db.session.commit()

                    a.clear()

                    a = []
                    if nontechis == '1':

                        if event6 == 'on':
                            if roll6:
                                flash("You already register for this event")
                                return render_template('register.html')
                            elif roll6 is None:
                                a.append('Event 6')
                                nontech_list = a
                                nontech_result = ','.join(nontech_list)
                                # print("TECH Result::",result)
                                new_reg = Event6(name=name, rollno=rollno, dept=dept, ieee=ieee,  email=email, event='event6', year=year,
                                                teamname=teamname, team_members=memember)
                                db.session.add(new_reg)
                                db.session.commit()

                        if event7 == 'on':
                            if roll7:
                                flash("You already register for this event")
                                return render_template('register.html')
                            elif roll7 is None:
                                a.append('Event 7')
                                nontech_list = a
                                nontech_result = ','.join(nontech_list)
                                # print("TECH Result::",result)
                                new_reg = Event7(name=name, rollno=rollno, dept=dept, ieee=ieee,  email=email, event='event7', year=year,
                                                teamname=teamname, team_members=memember)
                                db.session.add(new_reg)
                                db.session.commit()

                        if event8 == 'on':
                            if roll8:
                                flash("You already register for this event")
                                return render_template('register.html')
                            if roll8 is None:
                                a.append('Event 8')
                                print("\n","Event8::",a)
                                nontech_list = a
                                nontech_result = ','.join(nontech_list)
                                # print("TECH Result::",result)
                                new_reg = Event8(name=name, rollno=rollno, dept=dept, ieee=ieee,  email=email, event='event8', year=year,
                                                teamname=teamname, team_members=memember)
                                db.session.add(new_reg)
                                db.session.commit()

                        if event9 == 'on':
                            if roll9:
                                flash("You already register for this event")
                                return render_template('register.html')
                            a.append('Event 9')

                            limit = Event9.query.filter_by(id=20).first()
                            if limit:
                                flash("Team event is full")
                            if roll9 is None:
                                nontech_list = a
                                nontech_result = ','.join(nontech_list)
                                # print("TECH Result::",result)
                                new_reg = Event9(name=name, rollno=rollno, dept=dept, ieee=ieee,  email=email, event='event9', year=year,
                                                teamname=teamname, team_members=memember)
                                db.session.add(new_reg)
                                db.session.commit()

                        a.clear()

    

                if ieee == 'yes':
                    photoupload(pic=pic, techevent=result,
                                nontechevent=nontech_result, name=name, rollno=rollno)

                message = """Subject:Welcome to the IEEE Event \n\n
                            Welcome and thank you for registering for the IEEE Event {},{}. We're looking forward to an exciting and informative event.
                        
                            We hope to provide you with resources and information to further your knowledge and interests in the field of IEEE.
                        
                            Do not hesitate to reach out to us if you have any questions along the way!
                        
                            Sincerely,
                            The IEEE Team""".format(result, nontech_result)
                print(message)
                # send_mail(email= email,body=message)

                return render_template('response.html')


@auth.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':
        userName = request.form.get('username')
        password = request.form.get('pass')

        user = User.query.filter_by(id=1).first()

        if user.username == userName:

            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)

                return redirect(url_for('views.admin'))
            else:
                flash('Incorrect  password, try again.', category='error')
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
