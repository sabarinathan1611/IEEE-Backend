from flask import Blueprint, render_template, request, flash, jsonify,redirect, url_for
from flask_login import login_required, current_user


views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
def home():
    return render_template("index.html")
@views.route('/admin',methods=['GET','POST'])
@login_required
def admin():
    if (current_user.admin==True):
        flash("Welcome Admin")
    else:
     
        return redirect(url_for('auth.login'))
    return render_template("admin.html")

@views.route('/register',methods=['GET','POST'])
def register():
        return render_template('register.html')