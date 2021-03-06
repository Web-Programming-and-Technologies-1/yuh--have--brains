from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, EqualTo, Email

class SignUp(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('New Password', validators=[InputRequired(), EqualTo('confirm', message='Passwords must match')])
    confirm  = PasswordField('Repeat Password')
    submit = SubmitField('Sign Up', render_kw={'class': 'btn waves-effect waves-light white-text'})

class LogIn(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])
    submit = SubmitField('Login', render_kw={'class': 'btn waves-effect waves-light white-text'})   

class AddFriend(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    submit = SubmitField('Add', render_kw={'class': 'btn waves-effect waves-light white-text'})

class RemoveFriend(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    submit = SubmitField('Remove', render_kw={'class': 'btn waves-effect waves-light white-text'})

class SearchFriend(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    submit = SubmitField('Search', render_kw={'class': 'btn waves-effect waves-light white-text'})