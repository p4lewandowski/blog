from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {'username' : 'Carlos'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'What a fancy blog!'
        },
        {
            'author': {'username': 'Brad'},
            'body': 'Yea, I like it too!'
        }
    ]
    return render_template('index.html', title='Home', posts=posts, user=user)

@app.route('/login', methods=['GET', 'POST']) 
def login():
    form = LoginForm()
    # Skipped when validate returns False, which happens during GET as the form is not filled 
    if form.validate_on_submit():
        # Dummy placeholder to let the user know that the form worked 
        flash('Login requested for user {}, remember_me={}'.format(form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)
    