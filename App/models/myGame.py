from App.database import db

class MyGame(db.Model):
    __tablename__ = 'myGame'
    gameId = db.Column(db.Integer, primary_key=True)
    userId =  db.Column(db.Integer, db.ForeignKey('user.userId'), nullable=False)
    score = db.Column(db.Integer, nullable=False)
    leaderBoard = db.relationship('Leaderboard', backref=db.backref('leaderboard', lazy='joined'))
    
    def __init__(self, userId, score = 0):
        self.userId = userId
        self.score = score

    def toDict(self):
        return{
            'gameId': self.gameId,
            'userId': self.userId,
            'score': self.score
        }

    