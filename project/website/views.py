from flask import Flask, Blueprint, redirect, request, render_template, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from flask_login import login_required, current_user
from . import db
from .models import User, Closet, Item

views = Blueprint('views', __name__)

@views.route("/")
@login_required
def home():
    return render_template("indexwcss.html", user=current_user)

@views.route("/dashboard")
@login_required
def dashboard():
    return render_template("dashboardwcss.html", user=current_user)

@views.route("/closet")
@login_required
def closet():
    return render_template("closetwcss.html", user=current_user)

@views.route("/addItem", methods=['GET', 'POST'])
@login_required
def addItem():
    if request.method == 'POST':
        type = request.form.get('addType')
        color = request.form.get('addColor')
        style = request.form.get('addStyle')
        season = request.form.get('addSeason')
        fit = request.form.get('addFit')

    return render_template("additemwcss.html", user=current_user)

@views.route("/create-new-closet", methods=['GET', 'POST'])
@login_required
def addCloset():
    if request.method == 'POST':
        name = request.form.get('closetName')

        new_closet = Closet(closet_name=name, user_id=current_user.id)
        db.session.add(new_closet)
        db.session.commit()
    return render_template("createcloset.html", user=current_user)