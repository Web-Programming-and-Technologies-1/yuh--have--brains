from App.database import db

class Leaderboard(db.Model):
    boardId = db.Column(db.Integer, primary_key=True)
    gameId =  db.Column(db.Integer, db.ForeignKey('game.id'), nullable=False)
    communityId =  db.Column(db.Integer, db.ForeignKey('community.id'), nullable=False)
    

    def __init__(self, gameId, communityId):
        self.gameId = gameId
        self.communityId = communityId

    def toDict(self):
        return{
            'id': self.boardId,
            'gameId': self.gameId,
            'communityId': self.communityId
        }
