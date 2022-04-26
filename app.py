from flask import Flask, redirect
from flask.templating import render_template
from flask_wtf.csrf import CSRFProtect
from addFahrradFrom import AddFahrradForm
from addFahrradMarkenForm import AddFahrradMarkenForm
from addKundenForm import AddKundenForm
from addAusleihenForm import AddAusleihenForm
from model.models import Ausleihen, Fahrrad, Fahrradmarke, Kunden, db
import sqlalchemy

app = Flask(__name__)
app.secret_key = "VerySecretSecretKey"

@app.route("/", methods=["get","post"])
def base():
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
        newKunde.Email = addKundenForm.Email.data

        db.session.add(newKunde)
        db.session.commit()

        return redirect("/")
        
    
    items = db.session.query(Kunden).all()

    return render_template("index.html", \
        headline="Fahrrad-App", \
        form = addKundenForm, \
        items = items)


@app.route("/kunden.html")
def Kunden_requests():
    addKundenForm = AddKundenForm()
    items1 = db.session.query(Kunden).all()

    return render_template("/kunden.html", \
        headline1 = "Fahrrad-App", \
        form1 = addKundenForm, \
        items1 = items1)


@app.route("/", methods=["get","post"])
def base_1():
    addFahradForm = AddFahrradForm()
    
    if addFahradForm.validate_on_submit():
        print(addFahradForm.Model.data)
        print(addFahradForm.Farbe.data)
        print(addFahradForm.Reifen.data)
        print(addFahradForm.Preis.data)
        
        newFahrrad = Fahrrad()
        newFahrrad.Model = addFahradForm.Model.data
        newFahrrad.Farbe = addFahradForm.Farbe.data
        newFahrrad.Reifen = addFahradForm.Reifen.data
        newFahrrad.Preis = addFahradForm.Preis.data

        db.session.add(newFahrrad)
        db.session.commit()

        return redirect("/")
        
    
    items2 = db.session.query(Fahrrad).all()

    return render_template("index.html", \
        headline2 ="Fahrrad-App", \
        form2 = AddFahrradForm, \
        items2 = items2)


@app.route("/fahrrad.html")
def Fahrrad_requests():
    addFahrradForm = AddFahrradForm()
    items3 = db.session.query(Fahrrad).all()

    return render_template("/fahrrad.html", \
        headline3 = "Fahrrad-App", \
        form3 = addFahrradForm, \
        items3 = items3)


@app.route("/", methods=["get","post"])
def base_2():
    addFahrradMarkenForm = AddFahrradMarkenForm()
    
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

        return redirect("/")
        
    
    items4 = db.session.query(Fahrradmarke).all()

    return render_template("index.html", \
        headline4="Fahrrad-App", \
        form4 = AddFahrradMarkenForm, \
        items4 = items4)


@app.route("/fahrradMarke.html")
def FahrradMarke_requests():
    addFahrradMarkenForm = AddFahrradMarkenForm()
    items5 = db.session.query(Fahrradmarke).all()

    return render_template("/fahrradMarke.html", \
        headline5 = "Fahrrad-App", \
        form5 = addFahrradMarkenForm, \
        items5 = items5)


@app.route("/", methods=["get","post"])
def base_3():
    addAusleihenForm = AddAusleihenForm()
    
    if addAusleihenForm.validate_on_submit():
        print(addAusleihenForm.AusleiheDatum.data)
        print(addAusleihenForm.RückgabeDatum.data)
        
        newAusleihen = Ausleihen()
        newAusleihen.AusleiheDatum = addAusleihenForm.AusleiheDatum.data
        newAusleihen.RückgabeDatum = addAusleihenForm.RückgabeDatum.data

        db.session.add(newAusleihen)
        db.session.commit()

        return redirect("/")
        
    
    items6 = db.session.query(Ausleihen).all()

    return render_template("index.html", \
        headline6 ="Fahrrad-App", \
        form6 = AddAusleihenForm, \
        items6 = items6)

@app.route("/ausleihen.html")
def Ausleihen_requests():
    addAusleihenForm = AddAusleihenForm()
    items7 = db.session.query(Ausleihen).all()

    return render_template("/ausleihen.html", \
        headline7 = "Fahrrad-App", \
        form7 = addAusleihenForm, \
        items7 = items7)


app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:root@localhost/fahrradApp"

csrf = CSRFProtect(app)
db.init_app(app)

#blueprint fehlt

app.run(debug=True)