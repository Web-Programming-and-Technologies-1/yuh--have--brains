# from App.database import db

# class Community(db.Model):
#     communityId = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(120), nullable=False, unique=True)
#     gameId =  db.Column(db.Integer, db.ForeignKey('game.id'), nullable=False)
    

#     def __init__(self, gameId):
#         self.gameId = gameId

#     def toDict(self):
#         return{
#             'id': self.communityId,
#             'name': self.name,
#             'gameId': self.gameId
           
#         }

    