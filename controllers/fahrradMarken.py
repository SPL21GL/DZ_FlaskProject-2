from flask.templating import render_template
from flask import Blueprint, redirect, flash, request
from forms.addFahrradMarkenForm import AddFahrradMarkenForm
from model.models import db, Fahrradmarke
from forms.delete_FahrradMarken import DeleteForm_FahrradMarken
from forms.edit_Fahrradmarke import EditFahrradMarkenForm

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

        FahrradMarkeID_to_delete = delete_FahrradMarke.FahrradMarkenID.data
        FahrradMarke_to_delete = db.session.query(Fahrradmarke).filter(
            Fahrradmarke.FahrradMarkenID == FahrradMarkeID_to_delete)
        FahrradMarke_to_delete.delete()

        db.session.commit()

    else:
        print("Fatal Error")
    flash(f"FahrradMarke with id {FahrradMarkeID_to_delete} has been deleted")
    return redirect("/fahrradMarken")


@fahrradMarken_blueprint.route("/edit_fahrradMarke", methods=["post"])
def edit_FahrradMarken_base():
    edit_FahrradMarken = EditFahrradMarkenForm()

    if edit_FahrradMarken.validate_on_submit():
        print("Submit wurde durchgeführt")

        FahrradMarkenID = edit_FahrradMarken.FahrradMarkenID.data
        FahrradMarke_to_edit = db.session.query(Fahrradmarke).filter(
            Fahrradmarke.FahrradMarkenID == FahrradMarkenID).first()

        FahrradMarke_to_edit.MarkenName = edit_FahrradMarken.MarkenName.data
        FahrradMarke_to_edit.CEO = edit_FahrradMarken.CEO.data
        FahrradMarke_to_edit.Email = edit_FahrradMarken.Email.data
        FahrradMarke_to_edit.Standort = edit_FahrradMarken.Standort.data

        db.session.commit()

        return redirect("/fahrradMarken")

    else:
        raise ("Fatal Error")


@fahrradMarken_blueprint.route("/edit_fahrradMarke")
def showEditFahrradMarkenForm():

    FahrradMarkenID = request.args["FahrradMarkenID"]
    print(FahrradMarkenID)

    FahrradMarke_to_edit = db.session.query(Fahrradmarke).filter(
        Fahrradmarke.FahrradMarkenID == FahrradMarkenID).first()

    edit_FahrradMarke = EditFahrradMarkenForm()

    edit_FahrradMarke.FahrradMarkenID.data = FahrradMarke_to_edit.FahrradMarkenID
    edit_FahrradMarke.MarkenName.data = FahrradMarke_to_edit.MarkenName
    edit_FahrradMarke.CEO.data = FahrradMarke_to_edit.CEO
    edit_FahrradMarke.Email.data = FahrradMarke_to_edit.Email
    edit_FahrradMarke.Standort.data = FahrradMarke_to_edit.Standort

    return render_template("fahrradMarke/edit_fahrradMarke.html", form=edit_FahrradMarke)
