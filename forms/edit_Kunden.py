from flask_wtf import FlaskForm
from wtforms.fields.datetime import DateField
from wtforms.fields.simple import TextAreaField, HiddenField


class EditKundenForm(FlaskForm):
    KundenID = HiddenField("KundenID")
    VorName = TextAreaField("VorName")
    NachName = TextAreaField("NachName")
    Geburtsdatum = DateField("Geburtsdatum")
    Email = TextAreaField("Email")
