# from flask_sqlalchemy import SQLAlchemy
# from App.database import db
# db = SQLAlchemy()

# class Leaderboard(db.Model):
#     boardId = db.Column(db.Integer, primary_key=True)
#     gameId =  db.Column(db.Integer, db.ForeignKey('MyGame.gameId'), nullable=False)
#     communityId =  db.Column(db.Integer, db.ForeignKey('community.communityId'))
 
#     def toDict(self):
#         return{
#             'id': self.boardId,
#             'gameId': self.gameId,
#             'communityId': self.communityId
#         }
