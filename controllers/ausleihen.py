from flask.templating import render_template
from flask import Blueprint, redirect, flash, request
from forms.addAusleihenForm import AddAusleihenForm
from forms.delete_ausleihen import DeleteForm_Ausleihen
from model.models import db, Ausleihen
from forms.edit_ausleihen import EditAusleihenForm

ausleihen_blueprint = Blueprint('ausleihen_blueprint', __name__)


@ausleihen_blueprint.route("/ausleihen", methods=["get", "post"])
def ausleihen_base():
    addAusleihenForm = AddAusleihenForm()
    ausleihen = db.session.query(Ausleihen).all()

    if addAusleihenForm.validate_on_submit():
        print(addAusleihenForm.AusleiheDatum.data)
        print(addAusleihenForm.RückgabeDatum.data)

        newAusleihen = Ausleihen()
        newAusleihen.AusleiheDatum = addAusleihenForm.AusleiheDatum.data
        newAusleihen.RückgabeDatum = addAusleihenForm.RückgabeDatum.data

        db.session.add(newAusleihen)
        db.session.commit()

        return redirect("/ausleihen")

    return render_template("ausleihen/ausleihen.html",
                           form=addAusleihenForm,
                           ausleihen=ausleihen)

@ausleihen_blueprint.route("/ausleihen/delete", methods=["post"])
def del_ausleihen_base():
    delete_Ausleihen = DeleteForm_Ausleihen()
    if delete_Ausleihen.validate_on_submit():
        print("Gültig")

        Ausleihen_to_delete = delete_Ausleihen.AusleihenID.data
        Ausleihen_to_delete = db.session.query(Ausleihen).filter(
            Ausleihen.AusleihenID == Ausleihen_to_delete)
        Ausleihen_to_delete.delete()

        db.session.commit()

    else:
        print("Fatal Error")
    flash(f"Ausleihen with id {Ausleihen_to_delete} has been deleted")
    return redirect("/ausleihen")

@ausleihen_blueprint.route("/edit_ausleihen", methods=["post"])
def edit_ausleihen_base():
    edit_Ausleihen = EditAusleihenForm()

    if edit_Ausleihen.validate_on_submit():
        print("Submit wurde durchgeführt")

        AusleihenID = edit_Ausleihen.AusleihenID.data
        Ausleihen_to_edit = db.session.query(Ausleihen).filter(
            Ausleihen.AusleihenID == AusleihenID).first()

        Ausleihen_to_edit.AusleiheDatum = edit_Ausleihen.AusleiheDatum.data
        Ausleihen_to_edit.RückgabeDatum = edit_Ausleihen.RückgabeDatum.data
        Ausleihen_to_edit.KundenID = edit_Ausleihen.KundenID.data
        Ausleihen_to_edit.FahrradID = edit_Ausleihen.FahrradID.data

        db.session.commit()

        return redirect("/ausleihen")

    else:
        raise ("Fatal Error")


@ausleihen_blueprint.route("/edit_ausleihen")
def showEditAusleihenForm():

    AusleihenID = request.args["AusleihenID"]
    print(AusleihenID)

    Ausleihen_to_edit = db.session.query(Ausleihen).filter(
        Ausleihen.AusleihenID == AusleihenID).first()

    edit_Ausleihen = EditAusleihenForm()

    edit_Ausleihen.AusleihenID.data = Ausleihen_to_edit.AusleihenID
    edit_Ausleihen.AusleiheDatum.data = Ausleihen_to_edit.AusleiheDatum
    edit_Ausleihen.RückgabeDatum.data = Ausleihen_to_edit.RückgabeDatum
    edit_Ausleihen.KundenID.data = Ausleihen_to_edit.KundenID
    edit_Ausleihen.FahrradID.data = Ausleihen_to_edit.FahrradID

    return render_template("ausleihen/edit_ausleihen.html", form=edit_Ausleihen)
