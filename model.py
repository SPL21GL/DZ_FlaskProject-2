# coding: utf-8
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Kunden(db.Model):
    __tablename__ = 'kunden'


    KundenID = db.Column(db.Integer, primary_key=True, unique=True)