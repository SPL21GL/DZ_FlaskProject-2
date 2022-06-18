from flask_wtf import FlaskForm
from wtforms.fields.simple import TextAreaField, HiddenField
from wtforms.fields import DecimalField


class EditFahrradForm(FlaskForm):
    FahrradID = HiddenField("FahrradID")
    Model = TextAreaField("Model")
    Farbe = TextAreaField("Farbe")
    Reifen = TextAreaField("Reifen")
    Preis = DecimalField("Preis")
