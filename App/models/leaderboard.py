from App.database import db

class Leaderboard(db.Model):
    __tablename__ = 'leaderboard'
    boardId = db.Column(db.Integer, primary_key=True)
    gameId =  db.Column(db.Integer, db.ForeignKey('myGame.gameId'), nullable=False)
    communityId =  db.Column(db.Integer, db.ForeignKey('community.communityId'))
    

    def __init__(self, gameId, communityId):
        self.gameId = gameId
        self.communityId = communityId

    def toDict(self):
        return{
            'id': self.boardId,
            'gameId': self.gameId,
            'communityId': self.communityId
        }
