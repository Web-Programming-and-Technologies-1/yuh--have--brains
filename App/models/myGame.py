from App.database import db

class MyGame(db.Model):
    gameId = db.Column(db.Integer, primary_key=True)
    userId =  db.Column(db.Integer, db.ForeignKey('user.userId'), nullable=False)
    score = db.Column(db.Integer, nullable=False)
    
    
    def __init__(self, userId, score = 0):
        self.userId = userId
        self.score = score

    def toDict(self):
        return{
            'gameId': self.gameId,
            'userId': self.userId,
            'score': self.score
        }

    