from flask import render_template, flash, redirect
from application import app
from application.forms import LoginForm

@app.route('/')
def index():
    user = {'username': 'Daniel'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template(
        'index.html.jinja', 
        title='Home', 
        header='Home',
        user=user, 
        posts=posts
    )    

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(f'Login requested for user {form.username.data},'
              f' remember_me={form.remember_me.data}'
        )
        return redirect('/')
    return render_template('login.html.jinja', title='Sign In', form=form)
