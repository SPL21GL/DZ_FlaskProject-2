from flask_wtf import FlaskForm
from wtforms.fields.datetime import DateField


class AddAusleihenForm(FlaskForm):
    AusleiheDatum = DateField("AusleiheDatum")
    RückgabeDatum = DateField("AusleiheDatum")
