from app import app
from flask import render_template
from app.forms import Signupform

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
    return render_template('sign-up.html', form=form)