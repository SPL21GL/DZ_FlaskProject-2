
from flask import Flask, redirect, request, flash, session
from flask.templating import render_template
from flask import Blueprint
import sqlalchemy
from forms.addKundenForm import AddKundenForm
from model.models import db, Kunden

kunden_blueprint = Blueprint('kunden_blueprint', __name__)


@kunden_blueprint.route("/kunden", methods=["get", "post"])
def kunden_base():
    session: sqlalchemy.orm.scoping.scoped_session = db.session

    kunden = session.query(Kunden).all()
    return render_template("kunden/kunden.html",kunden= kunden)

    # addKundenForm = AddKundenForm()
    # kunden = db.session.query(Kunden).all()

    # if addKundenForm.validate_on_submit():
    #     print(addKundenForm.VorName.data)
    #     print(addKundenForm.NachName.data)
    #     print(addKundenForm.Geburtsdatum.data)
    #     print(addKundenForm.Email.data)

    #     newKunde = Kunden()
    #     newKunde.VorName = addKundenForm.VorName.data
    #     newKunde.NachName = addKundenForm.NachName.data
    #     newKunde.Geburtsdatum = addKundenForm.Geburtsdatum.data
    #     newKunde.Email = addKundenForm.Email.data

    #     db.session.add(newKunde)
    #     db.session.commit()

    #     return redirect("/kunden")

    # return render_template("kunden/kunden.html",
    #                        form=addKundenForm,
    #                        kunden=kunden)
