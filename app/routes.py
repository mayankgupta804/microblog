from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    user = {"username": "Mayank"}
    posts = [
        {
            'author':{'username':'Gaurav'},
            'body': 'Beautiful day in Bangalore!'
        },
        {
            'author':{'username':'Abhishek'},
            'body': 'Stree was a cool movie!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts) 