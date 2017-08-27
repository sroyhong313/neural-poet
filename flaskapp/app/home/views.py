# app/home/views.py

from flask import abort, render_template, jsonify
from flask_login import current_user, login_required
from subprocess import check_output

from app import poem_col
from . import sample
from . import home
from .. import *

@home.route('/')
def homepage():
    """
    Render the homepage template on the / route
    """
    return render_template('home/index.html', title="Welcome")

@home.route('/dashboard')
@login_required
def dashboard():
    """
    Render the dashboard template on the /dashboard route
    """
    return render_template('home/dashboard.html', title="Dashboard")

@home.route('/admin/dashboard')
@login_required
def admin_dashboard():
    # prevent non-admins from accessing this page
    if not current_user.is_admin:
        abort(403)

    return render_template('home/admin_dashboard.html', title="Dashboard-Admin")

@home.route('/make', methods=['GET','POST'])
def make():
    command = 'python3 app/home/sample.py -n 4000'
    while True:
        raw_text = check_output(command,shell=True)
        # try:
        #     raw_text = subprocess.check_output(command)
        # except subprocess.CalledProcessError as e:
        #     raw_text = e.output

        text = raw_text.decode('unicode_escape')
        poem = text.split('\n\n\n\n')
        if (len(poem) >= 3):
            poem = poem[1]
            break

    poem_col.insert({'textfield':poem})
    print (poem)
    poem = poem.split('\n')
    return render_template('home/new.html', title="New", poem=poem)
