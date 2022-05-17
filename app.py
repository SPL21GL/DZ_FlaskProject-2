from flask import Flask
from model.models import db
from controllers.index import index_blueprint
from controllers.kunden import kunden_blueprint


from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
app.secret_key = "VerySecretSecretKey"

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:root@localhost/fahrradApp"


csrf = CSRFProtect(app)

db.init_app(app)

app.register_blueprint(index_blueprint)
app.register_blueprint(kunden_blueprint)
app.register_blueprint(fahrrad_blueprint)
app.register_blueprint(fahrradMarke_blueprint)
app.register_blueprint(ausleihen_blueprint)

app.run(debug=True)
