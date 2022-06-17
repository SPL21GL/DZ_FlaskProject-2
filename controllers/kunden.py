from flask import redirect, flash, request
from flask.templating import render_template
from flask import Blueprint
from forms.addKundenForm import AddKundenForm
from model.models import db, Kunden
from forms.delete_Kunden import DeleteForm_Kunden
from forms.edit_Kunden import EditKundenForm

kunden_blueprint = Blueprint('kunden_blueprint', __name__)


@kunden_blueprint.route("/kunden", methods=["get", "post"])
def kunden_base():
    addKundenForm = AddKundenForm()
    kunden = db.session.query(Kunden).all()

    if addKundenForm.validate_on_submit():
        print(addKundenForm.VorName.data)
        print(addKundenForm.NachName.data)
        print(addKundenForm.Geburtsdatum.data)
        print(addKundenForm.Email.data)

        newKunde = Kunden()
        newKunde.VorName = addKundenForm.VorName.data
        newKunde.NachName = addKundenForm.NachName.data
        newKunde.Geburtsdatum = addKundenForm.Geburtsdatum.data
        newKunde.Email = addKundenForm.Email.data

        db.session.add(newKunde)
        db.session.commit()

        return redirect("/kunden")

    return render_template("kunden/kunden.html",
                           form=addKundenForm,
                           kunden=kunden)


@kunden_blueprint.route("/kunden/delete", methods=["post"])
def del_kunden_base():
    delete_Kunden = DeleteForm_Kunden()
    if delete_Kunden.validate_on_submit():
        print("Gültig")

        Kunde_to_delete = delete_Kunden.KundenID.data
        Kunde_to_delete = db.session.query(Kunden).filter(
            Kunden.KundenID == Kunde_to_delete)
        Kunde_to_delete.delete()

        db.session.commit()

    else:
        print("Fatal Error")
    flash(f"Kunde with id {Kunde_to_delete} has been deleted")
    return redirect("/kunden")


@kunden_blueprint.route("/kunden/edit", methods=["post"])
def edit_kunden_base():
    edit_Kunden = EditKundenForm()

    if edit_Kunden.validate_on_submit():
        print("Submit wurde durchgeführt")

        KundenID = edit_Kunden.KundenID.data
        Kunden_to_edit = db.session.query(Kunden).filter(
            Kunden.KundenID == KundenID).first()

        Kunden_to_edit.VorName = edit_Kunden.VorName.data
        Kunden_to_edit.NachName = edit_Kunden.NachName.data
        Kunden_to_edit.Geburtsdatum = edit_Kunden.Geburtsdatum.data
        Kunden_to_edit.Email = edit_Kunden.Email.data

        db.session.commit()

        return redirect("/kunden")

    else:
        raise ("Fatal Error")


@kunden_blueprint.route("/edit_kunden")
def showEditKundenForm():

    KundenID = request.args["KundenID"]
    print(KundenID)

    Kunde_to_edit = db.session.query(Kunden).filter(
        Kunden.KundenID == KundenID).first()

    edit_Kunden = EditKundenForm()

    edit_Kunden.KundenID.data = Kunde_to_edit.KundenID
    edit_Kunden.VorName.data = Kunde_to_edit.VorName
    edit_Kunden.NachName.data = Kunde_to_edit.NachName
    edit_Kunden.Geburtsdatum.data = Kunde_to_edit.Geburtsdatum
    edit_Kunden.Email.data = Kunde_to_edit.Email

    return render_template("kunden/edit_kunden.html", form=edit_Kunden)
