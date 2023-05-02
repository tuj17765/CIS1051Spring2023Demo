from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class Closet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    closet_name = db.Column(db.String(200), nullable=False)
    items = db.relationship('Item', backref='closet', lazy=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user_info.id'))

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(50))
    color = db.Column(db.String(50))
    season = db.Column(db.String(50))
    style = db.Column(db.String(50))
    fit = db.Column(db.String(50))
    closet_id = db.Column(db.Integer, db.ForeignKey('closet.id'))

class User(db.Model, UserMixin):
    __tablename__= 'user_info'
    id = db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.String(100))
    lastName = db.Column(db.String(100))
    userName = db.Column(db.String(30), unique=True)
    password = db.Column(db.String(15))
    closets = db.relationship('Closet')

