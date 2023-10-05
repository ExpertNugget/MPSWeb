from flask import Blueprint, render_template, request, flash
from email_validator import validate_email

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html', text='testing')

@auth.route('/logout')
def logout():
    return "<p>logout</p>"

@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form.get('email')
        username = request.form.get('username')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        if len(username) < 1:
            flash('Enter a username', category='error')
        elif password1 != password2:
            flash('passwords don\'t match', category='error')
        elif len(password1) < 8:
            flash('password must be at least 8 characters', category='error')
        else:
            flash('Account created!', category='success')
    return render_template('signup.html')