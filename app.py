from flask import Flask, redirect
from flask.templating import render_template
from flask_wtf.csrf import CSRFProtect
from addKundenForm import AddKundenForm
from model.models import Fahrrad, Kunden, db
import sqlalchemy

app = Flask(__name__)
app.secret_key = "VerySecretSecretKey"

@app.route("/")
def index():
    addKundenForm = AddKundenForm()
    
    if addKundenForm.validate_on_submit():
        print(addKundenForm.Vorname.data)
        print(addKundenForm.Nachname.data)
        print(addKundenForm.Geburtsdatum.data)
        print(addKundenForm.Email.data)
        
        newKunde = Kunden()
        newKunde.VorName = addKundenForm.Vorname.data
        newKunde.NachName = addKundenForm.Nachname.data
        newKunde.Geburtsdatum = addKundenForm.Geburtsdatum.data
        newKunde.isDone = addKundenForm.Email.data

        db.session.add(newKunde)
        db.session.commit()

        return redirect("/")
        
    
    kund = db.session.query(Kunden).all()

    return render_template("base.html", \
        headline="Fahrrad-App", \
        form = addKundenForm, \
        kund = Kunden)

@app.route("/kunden.html")
def Kunden_requests():
    addKundenForm = AddKundenForm()
    Kunde1 = db.session.query(Kunden).all()

    return render_template("/kunden.html", \
        headline = "Fahrrad-App", \
        form1 = addKundenForm, \
        items1 = Kunde1  )

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:root@localhost/fahrradApp"

csrf = CSRFProtect(app)
db.init_app(app)

#blueprint fehlt

app.run(debug=True)