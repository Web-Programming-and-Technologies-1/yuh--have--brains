# from flask_sqlalchemy import SQLAlchemy
# from App.database import db
# db = SQLAlchemy()

# class MyGame(db.Model):
#     gameId = db.Column(db.Integer, primary_key=True)
#     id =  db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
#     score = db.Column(db.Integer, nullable=False)
#     leaderBoard = db.relationship('Leaderboard', backref=db.backref('Leaderboard', lazy='joined'))

#     def toDict(self):
#         return{
#             'gameId': self.gameId,
#             'userId': self.userId,
#             'score': self.score
#         }

    