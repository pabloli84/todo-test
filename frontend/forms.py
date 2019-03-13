from flask_wtf import Form
from wtforms.fields import *
from wtforms.validators import DataRequired


class UserForm(Form):
    name = StringField(u'User Name', validators=[DataRequired()])

    submit = SubmitField(u'Add User')


class TasksForm(Form):
    task_name = StringField(u'Name')
    task_description = StringField(u'Description')
    task_assignee = StringField(u'Assignee')
    task_start_date = DateField(u'Start Date', format='%d-%m-%Y')
    task_end_date = DateField(u'End Date', format='%d-%m-%Y')

    submit = SubmitField(u'Add task')
