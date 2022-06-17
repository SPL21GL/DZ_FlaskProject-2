from flask_wtf import FlaskForm
from wtforms.fields.simple import HiddenField


class DeleteForm_FahrradMarken(FlaskForm):
    FahrradMarkenID = HiddenField("FahrradMarkenID")