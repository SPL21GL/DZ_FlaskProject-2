from flask.templating import render_template
from flask import Blueprint, redirect, flash
from forms.addFahrradMarkenForm import AddFahrradMarkenForm
from model.models import db, Fahrradmarke
from forms.delete_FahrradMarken import DeleteForm_FahrradMarken

fahrradMarken_blueprint = Blueprint('fahrradMarken_blueprint', __name__)


@fahrradMarken_blueprint.route("/fahrradMarken", methods=["get", "post"])
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

    return render_template("fahrradMarke/fahrradMarken.html",
                           form=addFahrradMarkenForm,
                           fahrradMarke=fahrradMarke)

@fahrradMarken_blueprint.route("/fahrradMarken/delete", methods=["post"])
def del_fahrradMarken_base():
    delete_FahrradMarke = DeleteForm_FahrradMarken()
    if delete_FahrradMarke.validate_on_submit():
        print("Gültig")

        FahrradMarke_to_delete = delete_FahrradMarke.FahrradMarkenID.data
        FahrradMarke_to_delete = db.session.query(Fahrradmarke).filter(
            Fahrradmarke.FahrradMarkenID == FahrradMarke_to_delete)
        FahrradMarke_to_delete.delete()

        db.session.commit()

    else:
        print("Fatal Error")
    flash(f"FahrradMarke with id {FahrradMarke_to_delete} has been deleted")
    return redirect("/fahrradMarken")
