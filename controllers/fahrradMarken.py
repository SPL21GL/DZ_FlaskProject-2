from flask.templating import render_template
from flask import Blueprint, redirect
from forms.addFahrradMarkenForm import AddFahrradMarkenForm
from model.models import db, Fahrradmarke

fahrradMarken_blueprint = Blueprint('fahrradMarken_blueprint', __name__)


@fahrradMarken_blueprint.route("/fahrradMarke", methods=["get", "post"])
def fahrradMarke_base():
    addFahrradMarkenForm = AddFahrradMarkenForm()
    fahrradMarke = db.session.query(Fahrradmarke).all()

    if addFahrradMarkenForm.validate_on_submit():
        print(addFahrradMarkenForm.MarkenName.data)
        print(addFahrradMarkenForm.CEO.data)
        print(addFahrradMarkenForm.Email.data)
        print(addFahrradMarkenForm.Standort.data)

        newFahrradMarke = Fahrradmarke()
        newFahrradMarke.MarkenName = addFahrradMarkenForm.MarkenName.data
        newFahrradMarke.CEO = addFahrradMarkenForm.CEO.data
        newFahrradMarke.Email = addFahrradMarkenForm.Email.data
        newFahrradMarke.Standort = addFahrradMarkenForm.Standort.data

        db.session.add(newFahrradMarke)
        db.session.commit()

        return redirect("/fahrradMarken")

    return render_template("fahrradMarke/fahrradMarke.html",
                           form=addFahrradMarkenForm,
                           fahrradMarke=fahrradMarke)
