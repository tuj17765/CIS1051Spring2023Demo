from flask import Blueprint, request, get_flashed_messages, render_template, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)

@auth.route("/login", methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        userName = request.form.get('userName')
        password = request.form.get('password')

        user_exists = User.query.filter_by(userName=userName).scalar() is not None

        print("user:", user_exists)

        if user_exists:
            user = User.query.filter_by(userName=userName).first()
            if check_password_hash(user.password, password):
                print('logged in successfully')
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password; try again!', category='error')
        else:
            flash('Email does not exist. Sign up?', category='error')

    return render_template("loginwcss.html", user=current_user)

@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == 'POST':
        firstName = request.form.get('firstName')
        lastName = request.form.get('lastName')
        userName = request.form.get('userName')
        password1 = request.form.get('pwd1')
        password2 = request.form.get('pwd2')

        user = User.query.filter_by(userName=userName).first()

        if user:
            flash('This username already exists.', category='error')
            print(userName, 'username already exists')
        elif userName is None or len(userName) < 5:
            flash('Username must be at least 4 characters.', category='error')
        elif len(firstName) < 2:
            flash('First name must be greater than 1 character.', category='error')
        elif password1 != password2:
            flash('Passwords do not match.', category='error')
        elif len(password1) < 3:
            flash('Password must be at least 5 characters', category='error')
        else:
            new_user = User(firstName=firstName, lastName=lastName, userName=userName, 
                            password=generate_password_hash(password1, method='sha256') )
            db.session.add(new_user)
            db.session.commit()
            
            login_user(user, remember=True)

            #flash('Account successfully created!', category='success')
            print('Account created')
            return redirect(url_for('views.home'))
        
    return render_template("signupwcss.html", user=current_user)
