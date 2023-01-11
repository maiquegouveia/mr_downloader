from mrdownloader import app, database, bcrypt
from flask import render_template, url_for, request, flash, redirect
from mrdownloader.forms import FormLogin, FormRegistration
from mrdownloader.models import User
from flask_login import login_user, login_required, logout_user, current_user

users_list = ['Maique', 'Viviane', 'Alon', 'João', 'Pedro', 'Everaldo']

@app.route('/')
def homepage():
    return render_template('homepage.html')

@app.route('/users')
@login_required
def users():
    return render_template('users.html', users_list=users_list)

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form_login = FormLogin(request.form)
    if form_login.validate_on_submit():
        user = User.query.filter_by(username=form_login.username.data).first()
        if user:
            if bcrypt.check_password_hash(user.password, form_login.password.data):
                login_user(user)
                flash(f"You have logged in the account: {form_login.username.data}", 'alert-success')
                next_arg = request.args.get('next')
                if next_arg:
                    return redirect(next_arg)
                else:
                    return redirect(url_for('homepage'))
            else:
                flash("Password incorrect", 'alert-danger')
        else:
            flash(f"This username is not registered", 'alert-danger')
    return render_template('sign_in.html', form_login=form_login)

@app.route('/registration', methods=['get', 'post'])
def register():
    form_registration = FormRegistration()
    if form_registration.validate_on_submit():
        password_crypt = bcrypt.generate_password_hash(form_registration.password.data)
        user = User(
            username=form_registration.username.data,
            password=password_crypt
        )
        database.session.add(user)
        database.session.commit()
        flash(f"You have registered as {form_registration.username.data}", 'alert-success')
        login_user(user)
        return redirect(url_for('homepage'))
    return render_template('registration.html', form_registration=form_registration)

@app.route('/profile')
@login_required
def profile():
    profile_picture = url_for('static', filename='profile_pictures/{}'.format(current_user.profile_picture))
    return render_template('profile.html', profile_picture=profile_picture)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash("You have logged out from the account", 'alert-warning')
    return redirect(url_for('homepage'))