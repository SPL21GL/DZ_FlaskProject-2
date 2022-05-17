from flask.templating import render_template
from flask import Blueprint
from forms.addFahrradFrom import AddFahrradForm
from model.models import db, Fahrrad

fahrrad_blueprint = Blueprint('fahrrad_blueprint', __name__)


@fahrrad_blueprint.route("/Fahrrad.html", methods=["get", "post"])
def kunden():
    addFahrradForm = AddFahrradForm()
    items3 = db.session.query(Fahrrad).all()

    if addFahrradForm.validate_on_submit():
        print(addFahrradForm.Model.data)
        print(addFahrradForm.Farbe.data)
        print(addFahrradForm.Reifen.data)
        print(addFahrradForm.Preis.data)

        newFahrrad = Fahrrad()
        newFahrrad.Model = addFahrradForm.Model.data
        newFahrrad.Farbe = addFahrradForm.Farbe.data
        newFahrrad.Reifen = addFahrradForm.Reifen.data
        newFahrrad.Preis = addFahrradForm.Preis.data

        db.session.add(newFahrrad)
        db.session.commit()

    return render_template("/fahrrad.html",
                           headline3="Fahrrad-App",
                           form3=addFahrradForm,
                           items3=items3)
