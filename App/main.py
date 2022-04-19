import os
from flask import Flask, request, render_template, flash, redirect, url_for
from flask_jwt import JWT, jwt_required, current_identity
from flask_login import LoginManager, current_user, login_user, login_required
from flask_uploads import DOCUMENTS, IMAGES, TEXT, UploadSet, configure_uploads
from flask_cors import CORS
from werkzeug.utils import secure_filename
from werkzeug.datastructures import  FileStorage
from datetime import timedelta

from random_word import RandomWords

from .models import db , User, Friend, MyGame
from .forms import SignUp, LogIn, AddFriend


from App.database import create_db, get_migrate

from App.controllers import (
    setup_jwt
)

from App.views import (
    user_views,
    api_views
)

views = [
    user_views,
    api_views
]

def add_views(app, views):
    for view in views:
        app.register_blueprint(view)


def loadConfig(app, config):
    app.config['ENV'] = os.environ.get('ENV', 'DEVELOPMENT')
    if app.config['ENV'] == "DEVELOPMENT":
        app.config.from_object('App.config')
    else:
        app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI')
        app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
        app.config['JWT_EXPIRATION_DELTA'] =  timedelta(days=int(os.environ.get('JWT_EXPIRATION_DELTA')))
        app.config['DEBUG'] = os.environ.get('ENV').upper() != 'PRODUCTION'
        app.config['ENV'] = os.environ.get('ENV')
    for key, value in config.items():
        app.config[key] = config[key]

def create_app(config={}):
    app = Flask(__name__, static_url_path='/static')
    CORS(app)
    loadConfig(app, config)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.config['PREFERRED_URL_SCHEME'] = 'https'
    app.config['UPLOADED_PHOTOS_DEST'] = "App/uploads"
    photos = UploadSet('photos', TEXT + DOCUMENTS + IMAGES)
    configure_uploads(app, photos)
    add_views(app, views)
    create_db(app)
    setup_jwt(app)
    app.app_context().push()
    return app

app = create_app()
migrate = get_migrate(app)

''' Begin Flask Login Functions '''
login_manager = LoginManager(app)
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)
''' End Flask Login Functions '''

def authenticate(uname, password):
  #search for the specified user
  user = User.query.filter_by(username=uname).first()
  #if user is found and password matches
  if user and user.check_password(password):
    return user

#Payload is a dictionary which is passed to the function by Flask JWT
def identity(payload):
  return User.query.get(payload['identity'])

jwt = JWT(app, authenticate, identity)

@app.before_first_request
def create_tables():
    db.create_all()
    db.session.commit()

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/signup', methods=['GET'])
def signup():
  form = SignUp() # create form object
  return render_template('signUp.html', form=form) # pass form object to template

@app.route('/signup', methods=['POST'])
def signupAction():
  form = SignUp() # create form object
  if form.validate_on_submit():
    data = request.form # get data from form submission
    newuser = User(username=data['username']) # create user object
    newuser.set_password(data['password']) # set password
    db.session.add(newuser) # save new user
    db.session.commit()
    flash('Account Created!')# send message
    return render_template('index.html')
  flash('Error invalid input!')
  return render_template('signUp.html', form = form)

@app.route('/main', methods=['GET'])
@login_required
def tomain():
#   form = Login() # create form object
  return render_template('main.html') # pass form object to template

@app.route('/community', methods=['GET'])
@login_required
def tocommunity():
#   form = Login() # create form object
  return render_template('community.html') # pass form object to template

@app.route('/playgame', methods=['GET'])
@login_required
def toplaygame():
  r = RandomWords()
  wordbank = []
  for x in range(20):
    wordbank.append(r.get_random_word())
    print(wordbank[x])
  return render_template('playgame.html', wordbank = wordbank) # pass form object to template

@app.route('/login', methods=['GET'])
def login():
  form = LogIn()
  return render_template('login.html', form=form)

#user submits the login form
@app.route('/login', methods=['POST'])
def loginAction():
  form = LogIn()
  if form.validate_on_submit(): # respond to form submission
      data = request.form
      user = User.query.filter_by(username = data['username']).first()
      if user and user.check_password(data['password']): # check credentials
        flash('Logged in successfully.') # send message to next page
        login_user(user) # login the user
        return render_template('main.html') # redirect to main page if login successful
  flash('Invalid credentials')
  return render_template('login.html',form =form)

@app.route('/add', methods=['GET'])
@login_required
def add():
  form = AddFriend() # create form object
  return render_template('addfriend.html', form=form) # pass form object to template

@app.route('/add', methods=['POST'])
@login_required
def addAction():
  form = AddFriend() # create form object
  if form.validate_on_submit(): # respond to form submission
      data = request.form
      user = User.query.filter_by(username = data['username']).first()
      if user:
        friend = Friend(fid = user.id, name = user.username, id = current_identity.id)
        db.session.add(friend)
        db.session.commit()
        return render_template('community.html') # pass form object to template
      return render_template('addfriend.html', form=form)

@app.route('/remove', methods=['GET'])
@login_required
def toremove():
#   form = Login() # create form object
  return render_template('removefriend.html') # pass form object to template

@app.route('/search', methods=['GET'])
@login_required
def tosearch():
#   form = Login() # create form object
  return render_template('searchfriend.html') # pass form object to template

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080, debug=True)