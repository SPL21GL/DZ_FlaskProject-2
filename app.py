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
        print(addKundenForm.VorName.data)
        print(addKundenForm.NachName.data)
        print(addKundenForm.Geburtsdatum.data)
        print(addKundenForm.Email.data)
        
        newKunde = Kunden()
        newKunde.VorName = addKundenForm.VorName.data
        newKunde.NachName = addKundenForm.NachName.data
        newKunde.Geburtsdatum = addKundenForm.Geburtsdatum.data
        newKunde.isDone = addKundenForm.Email.data

        db.session.add(newKunde)
        db.session.commit()

        return redirect("/")
        
    
    kund = db.session.query(Kunden).all()

    return render_template("index.html", \
        headline="Fahrrad-App", \
        form = addKundenForm, \
        kund = Kunden)


app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:root@localhost/fahrradApp"

csrf = CSRFProtect(app)
db.init_app(app)

app.run(debug=True)