from flask_wtf import FlaskForm
from wtforms.fields.simple import HiddenField
from wtforms.fields.datetime import DateField


class EditAusleihenForm(FlaskForm):
    AusleihenID = HiddenField("AusleihenID")
    AusleiheDatum = DateField("AusleiheDatum")
    RückgabeDatum = DateField("RückgabeDatum")
    KundenID = HiddenField("KundenID")
    FahrradID = HiddenField("FahrradID")
