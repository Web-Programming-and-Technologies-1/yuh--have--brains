from App.models import User
from App.models import Community
from App.models import Leaderboard
from App.models import MyGame

   # controllers
def display_highest_score(username, score):
    
    return

def display_history(username):
    return

def delete_friend(userId):
    user = Community.Users.query.get(userId)
    db.session.delete(user)
    db.session.commit()

def add_friend(userId):
    user = Community.Users.query.get(userId)
    db.session.add(user)
    db.session.commit()