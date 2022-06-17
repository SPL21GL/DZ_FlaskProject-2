from flask_wtf import FlaskForm
from wtforms.fields.datetime import DateField
from wtforms.fields.simple import StringField
from wtforms import validators


class AddAusleihenForm(FlaskForm):
    AusleiheDatum = DateField("AusleiheDatum")
    RückgabeDatum = DateField("AusleiheDatum")
