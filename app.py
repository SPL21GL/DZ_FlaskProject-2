from flask import Flask
from flask.templating import render_template
from flask_wtf.csrf import CSRFProtect
from model.models import db
import sqlalchemy

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", headline = "Fahrrad-App")

app.secret_key = "VerySecretSecretKey"

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:root@localhost/fahrradApp"

csrf = CSRFProtect(app)
db.init_app(app)

app.run(debug=True)