from flask.templating import render_template
from flask import Blueprint
from forms.addKundenForm import AddKundenForm
from model.models import db, Kunden

kunden_blueprint = Blueprint('kunden_blueprint', __name__)


@kunden_blueprint.route("/Kunden.html", methods=["get", "post"])
def kunden():
    addKundenForm = AddKundenForm()
    items = db.session.query(Kunden).all()

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

    return render_template("/kunden.html",
                           headline1="Fahrrad-App",
                           form1=addKundenForm,
                           items=items)
