from flask_wtf import FlaskForm
from wtforms.fields.datetime import DateField
from wtforms.fields.simple import StringField, TextAreaField
from wtforms import validators

class AddKundenForm(FlaskForm):
    Vorname = StringField("VorName",  validators=[validators.InputRequired()])
    Nachname = StringField("NachName",  validators=[validators.InputRequired()])
    Geburtsdatum = DateField("Geburtsdatum")
    Email = StringField("Email",  validators=[validators.InputRequired()])