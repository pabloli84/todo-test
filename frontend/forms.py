from flask_wtf import Form
from wtforms.fields import *
from wtforms.validators import DataRequired


class UserForm(Form):
    name = StringField(u'User Name', validators=[DataRequired()])

    submit = SubmitField(u'Add User')
