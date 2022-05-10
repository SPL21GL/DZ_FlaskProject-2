from flask import Flask, redirect, request
from flask.templating import render_template
from flask import Blueprint
import sqlalchemy
import sqlalchemy.orm

from model.models import Kunden, db

kunden_blueprint = Blueprint('kunden_blueprint', __name__)

@kunden_blueprint.route("/kunden")
def kunden():
   
    session: sqlalchemy.orm.scoping.scoped_session = db.session

    #skunden = session.query(Kunden).Kunden(Kunden.orderNumber).all()

    return render_template("kunden/kunden.html", kunden=kunden)
