from flask.templating import render_template
from flask import Blueprint, redirect, flash
from forms.addAusleihenForm import AddAusleihenForm
from forms.delete_ausleihen import DeleteForm_Ausleihen
from model.models import db, Ausleihen

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
