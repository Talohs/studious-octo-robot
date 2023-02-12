from app import app
from flask import render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required, current_user
from app.forms import Signupform, LoginForm, AddressForm
from app.models import User, Address

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/sign_up", methods=['GET', 'POST'])
def signup():
    form = Signupform()
    if form.validate_on_submit():
        print('Form submitted and validated')
        first_name = form.first_name.data
        last_name = form.last_name.data
        email = form.email.data
        username = form.username.data
        password = form.password.data
        print(first_name, last_name, email, username, password)

        check_user = User.query.filter( (User.email==email) | (User.username==username)).all()

        if check_user:
            flash('A user with that email and/or username already exists.', 'danger')
            return redirect(url_for('signup'))

        new_user = User(first_name=first_name, last_name=last_name, email=email, username=username, password=password)

        flash(f'Thank you {new_user.username} for using our app!', 'success')

        return redirect(url_for('index'))

    return render_template('sign-up.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # Get the username and password from the form
        username = form.username.data
        password = form.password.data
        print(username, password)
        # Query the user table to see if there is a user with that username
        user = User.query.filter_by(username=username).first()
        # Check if there is a user and that the password is correct
        if user is not None and user.check_password(password):
            # log the user in
            login_user(user)
            flash(f"{user.username} is now logged in", "warning")
            return redirect(url_for('index'))
        else:
            flash("Incorrect username and/or password", "danger")
            return redirect(url_for('login'))
        
    return render_template('login.html', form=form)

@app.route('/logout')
def logout():
    logout_user()
    flash("You have been logged out", "warning")
    return redirect(url_for('index'))

@app.route('/create', methods=['Post'])
def create_address():
    form = AddressForm()
    if form.validate_on_submit():
        first_name = form.first_name.data
        last_name = form.last_name.data
        phone_number = form.phone_number.data
        address = form.address.data
        new_address = Address(first_name=first_name, last_name=last_name,phone_number=phone_number,address=address)
        flash(f"{new_address.first_name} {new_address.last_name}'s has been created", "succes")
        return redirect(url_for('index'))


    return render_template('create.html', form=form)