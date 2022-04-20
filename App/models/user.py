from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import UserMixin
db = SQLAlchemy()

class User(db.Model, UserMixin):
    __tablename__ = 'User'
    id = db.Column(db.Integer, primary_key=True)
    username =  db.Column(db.String, unique = True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    friends = db.relationship('Friend', cascade="all, delete-orphan")
    myGames = db.relationship('MyGame', cascade="all, delete-orphan")

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

class Friend(db.Model):
    __tablename__ = 'Friend'
    fid = db.Column(db.Integer, primary_key=True)
    id = db.Column('id', db.Integer, db.ForeignKey('User.id'))
    name = db.Column(db.String(120), nullable=False, unique=True)
    score = db.Column(db.Integer, nullable = True)
    
    def __init__(self, fid, id, name, score):
        self.fid = fid
        self.id = id
        self.name = name
        self.score = score

    def toDict(self):
        return{
            'fid': self.fid,
            'username': self.username,
            'id': self.id
        }

# class Leaderboard(db.Model):
#     boardId = db.Column(db.Integer, primary_key=True)
#     communityId =  db.Column(db.Integer, db.ForeignKey('community.communityId'))
 
#     def toDict(self):
#         return{
#             'id': self.boardId,
#             'gameId': self.gameId,
#             'communityId': self.communityId
#         }

class MyGame(db.Model):
    __tablename = 'MyGame'
    gameId = db.Column(db.Integer, primary_key=True)
    id =  db.Column(db.Integer, db.ForeignKey('User.id'), nullable=False)
    score = db.Column(db.Integer, nullable=False)

    def toDict(self):
        return{
            'gameId': self.gameId,
            'userId': self.userId,
            'score': self.score
        }
