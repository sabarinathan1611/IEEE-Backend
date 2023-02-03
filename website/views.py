from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user


views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
def home():
    return render_template("index.html")
@views.route('/admin',methods=['GET','POST'])
@login_required
def admin():
    return render_template("admin.html")

