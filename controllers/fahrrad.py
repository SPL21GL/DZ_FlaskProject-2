from flask import redirect, flash, request, render_template
from flask import Blueprint
from forms.addFahrradFrom import AddFahrradForm
from forms.delete_Fahrrad import DeleteForm_Fahrrad
from model.models import db, Fahrrad

fahrrad_blueprint = Blueprint('fahrrad_blueprint', __name__)


@fahrrad_blueprint.route("/fahrrad", methods=["get", "post"])
def fahrrad_base():
    addFahrradForm = AddFahrradForm()
    fahrrad = db.session.query(Fahrrad).all()

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

        return redirect("/fahrrad")

    return render_template("fahrrad/fahrrad.html",
                           form=addFahrradForm,
                           fahrrad=fahrrad)


@fahrrad_blueprint.route("/fahrrad/delete", methods=["post"])
def del_fahrrad_base():
    delete_Fahrrad = DeleteForm_Fahrrad()
    if delete_Fahrrad.validate_on_submit():
        print("Gültig")

        Fahrrad_to_delete = delete_Fahrrad.FahrradID.data
        Fahrrad_to_delete = db.session.query(Fahrrad).filter(
            Fahrrad.FahrradID == Fahrrad_to_delete)
        Fahrrad_to_delete.delete()

        db.session.commit()

    else:
        print("Fatal Error")
    flash(f"Fahrrad with id {Fahrrad_to_delete} has been deleted")
    return redirect("/fahrrad")
