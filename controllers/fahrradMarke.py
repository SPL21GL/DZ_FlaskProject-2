from flask.templating import render_template
from flask import Blueprint
from forms.addFahrradMarkenForm import AddFahrradMarkenForm
from model.models import db, Fahrradmarke

fahrradMarken_blueprint = Blueprint('fahrradmarken_blueprint', __name__)


@fahrradMarken_blueprint.route("/FahrradMarken.html", methods=["get", "post"])
def kunden():
    addFahrradMarkenForm = AddFahrradMarkenForm()
    items5 = db.session.query(Fahrradmarke).all()

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

    return render_template("/fahrradMarke.html",
                           headline5="Fahrrad-App",
                           form5=addFahrradMarkenForm,
                           items5=items5)
