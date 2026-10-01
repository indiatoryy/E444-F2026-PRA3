# render_template opens the html files
# session remembers the name and email in this browser
# redirect and url_for send the browser back to the home page
# flash is how I show the yellow "you changed your name" messages
from flask import Flask, render_template, session, redirect, url_for, flash

from flask_bootstrap import Bootstrap # this is for the nav bar
from flask_moment import Moment # this is for the date from activity 1.3
from flask_wtf import FlaskForm # this is the form class from chapter 4
from wtforms import StringField, SubmitField, EmailField
from wtforms.validators import DataRequired, Email

# this makes the app
app = Flask(__name__)
# flask needs a secret key or the form and the session will not work
# the textbook just uses this string
app.config['SECRET_KEY'] = 'hard to guess string'

# hook bootstrap and moment up to the app
bootstrap = Bootstrap(app)
moment = Moment(app)


# this is the form on the home page
class NameForm(FlaskForm):
    # DataRequired means the box cannot be left empty
    name = StringField('What is your name?', validators=[DataRequired()])
    # EmailField makes the browser check for an @ sign
    # Email() checks it again on the server
    email = EmailField('What is your UofT Email address?', validators=[DataRequired(), Email()])
    submit = SubmitField('Submit')


# this runs when someone goes to a url that does not exist
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


# this runs if the app crashes
@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


# GET is just opening the page. POST is clicking Submit.
@app.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    # this is only true if they clicked submit and both boxes are valid
    if form.validate_on_submit():
        # look up what we saved last time, if anything
        old_name = session.get('name')
        old_email = session.get('email')
        # only warn them if they already had a name and typed a new one
        if old_name is not None and old_name != form.name.data:
            flash('Looks like you have changed your name!')
        if old_email is not None and old_email != form.email.data:
            flash('Looks like you have changed your email!')
        # save the new answers. form.name.data is whatever they typed
        session['name'] = form.name.data
        session['email'] = form.email.data
        # send them back to this same page so a refresh does not submit twice
        return redirect(url_for('index'))
    # if they have not submitted yet, name and email are empty
    # then the template says Hello, Stranger!
    return render_template('index.html', form=form, name=session.get('name'), email=session.get('email'))


# this is the old example 2-2 page, like /user/India
@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, {}!</h1>'.format(name)


# only start the server when I run this file, not when it gets imported
if __name__ == '__main__':
    app.run(debug=True)
