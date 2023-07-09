from flask import render_template
from app import app

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
    