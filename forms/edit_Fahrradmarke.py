from flask_wtf import FlaskForm
from wtforms.fields.simple import TextAreaField, HiddenField


class EditFahrradMarkenForm(FlaskForm):
    FahrradMarkenID = HiddenField("FahrradMarkenID")
    MarkenName = TextAreaField("MarkenName")
    CEO = TextAreaField("CEO")
    Email = TextAreaField("Email")
    Standort = TextAreaField("Standort")
