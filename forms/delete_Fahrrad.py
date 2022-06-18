from flask_wtf import FlaskForm
from wtforms.fields.simple import HiddenField


class DeleteForm_Fahrrad(FlaskForm):
    FahrradID = HiddenField("FahrradID")
