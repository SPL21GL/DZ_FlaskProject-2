from flask_wtf import FlaskForm
from wtforms.fields.simple import StringField
from wtforms import validators


class AddFahrradMarkenForm(FlaskForm):
    MarkenName = StringField("MarkenName",  validators=[
                             validators.InputRequired()])
    CEO = StringField("CEO", validators=[validators.InputRequired()])
    Email = StringField("Email",  validators=[validators.InputRequired()])
    Standort = StringField("Standort",  validators=[
                           validators.InputRequired()])
