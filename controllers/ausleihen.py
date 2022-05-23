from flask.templating import render_template
from flask import Blueprint
from forms.addAusleihenForm import AddAusleihenForm
from model.models import db, Ausleihen

ausleihen_blueprint = Blueprint('ausleihen_blueprint', __name__)


@ausleihen_blueprint.route("/ausleihen.html", methods=["get", "post"])
def ausleihen_base():
    addAusleihenForm = AddAusleihenForm()
    items7 = db.session.query(Ausleihen).all()

    if addAusleihenForm.validate_on_submit():
        print(addAusleihenForm.AusleiheDatum.data)
        print(addAusleihenForm.RückgabeDatum.data)

        newAusleihen = Ausleihen()
        newAusleihen.AusleiheDatum = addAusleihenForm.AusleiheDatum.data
        newAusleihen.RückgabeDatum = addAusleihenForm.RückgabeDatum.data

        db.session.add(newAusleihen)
        db.session.commit()

    return render_template("/ausleihen.html",
                           headline7="Fahrrad-App",
                           form7=addAusleihenForm,
                           items7=items7)
