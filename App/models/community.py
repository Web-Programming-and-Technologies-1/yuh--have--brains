# from flask_sqlalchemy import SQLAlchemy
# from App.database import db
# db = SQLAlchemy()

# class Community(db.Model):
#     communityId = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(120), nullable=False, unique=True)
#     # gameId =  db.Column(db.Integer, db.ForeignKey('game.id'), nullable=False)
#     Users = db.relationship('User', backref=db.backref('Community', lazy='joined'))
    
#     def toDict(self):
#         return{
#             'id': self.communityId,
#             'name': self.name,
#             'gameId': self.gameId,
#            'users': [user.toDict() for user in self.Users]
#         }

    