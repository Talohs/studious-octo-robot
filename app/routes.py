from app import app
from flask import render_template, redirect, url_for, flash
from app.forms import Signupform
from app.models import User

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/posts')
def posts():
    return 'These are the posts!'

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
        return redirect(url_for('index'))
    return render_template('sign-up.html', form=form)