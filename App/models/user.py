from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import UserMixin
db = SQLAlchemy()

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username =  db.Column(db.String, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    # communityId =  db.Column(db.Integer, db.ForeignKey('community.communityId'))
    # myGames = db.relationship('MyGame', backref=db.backref('MyGame', lazy='joined'))
    # gamesPlayed = db.relationship('MyGame', backref='user', lazy=True, cascade="all, delete-orphan")

    def __init__(self, username):
        self.username = username
        # self.set_password(password)

    def toDict(self):
        return{
            'id': self.userId,
            'username': self.username,
            'myGames': [myGame.toDict() for myGame in self.MyGame]
        }

    def set_password(self, password):
        """Create hashed password."""
        self.password = generate_password_hash(password, method='sha256')
    
    def check_password(self, password):
        """Check hashed password."""
        return check_password_hash(self.password, password)

# class Community(db.Model):
#     communityId = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(120), nullable=False, unique=True)
#     # gameId =  db.Column(db.Integer, db.ForeignKey('game.id'), nullable=False)
#     users = db.relationship('User', backref=db.backref('Community', lazy='joined'))
    
#     def toDict(self):
#         return{
#             'id': self.communityId,
#             'name': self.name,
#             'gameId': self.gameId,
#            'users': [user.toDict() for user in self.Users]
#         }

# class Leaderboard(db.Model):
#     boardId = db.Column(db.Integer, primary_key=True)
#     communityId =  db.Column(db.Integer, db.ForeignKey('community.communityId'))
 
#     def toDict(self):
#         return{
#             'id': self.boardId,
#             'gameId': self.gameId,
#             'communityId': self.communityId
#         }

# class MyGame(db.Model):
#     gameId = db.Column(db.Integer, primary_key=True)
#     id =  db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
#     score = db.Column(db.Integer, nullable=False)

#     def toDict(self):
#         return{
#             'gameId': self.gameId,
#             'userId': self.userId,
#             'score': self.score
#         }
