from flask_wtf import FlaskForm
from wtforms.fields.simple import HiddenField


class DeleteForm_Kunden(FlaskForm):
    KundenID = HiddenField("KundenID")
