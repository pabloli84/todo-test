from flask import Blueprint, render_template, flash, redirect, url_for
from flask_nav.elements import Navbar, View, Subgroup, Link, Text, Separator
from markupsafe import escape
from .client import add_user

from .forms import UserForm, TasksForm
from .nav import nav

frontend = Blueprint('frontend', __name__)


nav.register_element('frontend_top', Navbar(
    View('Home', '.index'),
    View('Users', '.users'),
    View('Tasks', '.tasks')
    ))


# Homepage
@frontend.route('/')
def index():
    return render_template('index.html')


# Shows a long signup form, demonstrating form rendering.
@frontend.route('/users/', methods=('GET', 'POST'))
def users():
    form = UserForm()

    if form.is_submitted():

        # if form.validate_on_submit():
            # flash('Hello, {}. You have successfully signed up'
            #       .format(escape(form.name.data)))
            #
            # # In a real application, you may wish to avoid this tedious redirect.
        print("User: ", form.name.data)
        status_code, message = add_user(escape(form.name.data))

        if status_code == 201:
            flash('User {} successfully added!'
                  .format(escape(form.name.data)))
        else:
            flash('Error adding user: {}'.format(message))
        return redirect(url_for('.index'))

    return render_template('users.html', form=form)


@frontend.route('/tasks/', methods=('GET', 'POST'))
def tasks():
    form = TasksForm()

    return render_template('tasks.html', form=form)
