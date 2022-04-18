from App.models import User
from App.models import Community
from App.models import Leaderboard
from App.models import MyGame
from sqlalchemy import func

   # controllers
def display_highest_score(username):
    return db.session.query(func.max(MyGame.score))

def display_history(username):
    return username.myGame

def delete_friend(userId):
    user = Community.Users.query.get(userId)
    db.session.delete(user)
    db.session.commit()

def add_friend(userId):
    user = Community.Users.query.get(userId)
    db.session.add(user)
    db.session.commit()