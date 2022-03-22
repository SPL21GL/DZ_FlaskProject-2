# coding: utf-8
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()



class Ausleihen(db.Model):
    __tablename__ = 'ausleihen'

    AusleihenID = db.Column(db.Integer, primary_key=True, unique=True)
    AusleiheDatum = db.Column(db.Date, nullable=False)
    RückgabeDatum = db.Column(db.Date, nullable=False)
    KundenID = db.Column(db.Integer)
    FahrradIdD = db.Column(db.Integer)



class Fahrrad(db.Model):
    __tablename__ = 'fahrrad'

    FahrradID = db.Column(db.Integer, primary_key=True, unique=True)
    Model = db.Column(db.String(64), nullable=False)
    Farbe = db.Column(db.String(32), nullable=False)
    Reifen = db.Column(db.String(128), nullable=False)
    Preis = db.Column(db.Numeric(10, 0), nullable=False)



class Fahrradmarke(db.Model):
    __tablename__ = 'fahrradmarke'

    FahrradMarkenID = db.Column(db.Integer, primary_key=True, unique=True)
    FahrradID = db.Column(db.ForeignKey('fahrrad.FahrradID'), index=True)
    MarkenName = db.Column(db.String(64), nullable=False)
    CEO = db.Column(db.String(64), nullable=False)
    Email = db.Column(db.String(64), nullable=False)
    Standort = db.Column(db.String(128), nullable=False)

    fahrrad = db.relationship('Fahrrad', primaryjoin='Fahrradmarke.FahrradID == Fahrrad.FahrradID', backref='fahrradmarkes')



class Kunden(db.Model):
    __tablename__ = 'kunden'

    KundenID = db.Column(db.Integer, primary_key=True, unique=True)
    VorName = db.Column(db.String(64), nullable=False)
    NachName = db.Column(db.String(64), nullable=False)
    Geburtsdatum = db.Column(db.Date, nullable=False)
    Email = db.Column(db.String(64), nullable=False)


    