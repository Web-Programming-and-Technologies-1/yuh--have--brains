from App.database import db

class Community(db.Model):
    __tablename__ = 'community'
    communityId = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False, unique=True)
    # gameId =  db.Column(db.Integer, db.ForeignKey('game.id'), nullable=False)
    Users = db.relationship('User', backref=db.backref('community', lazy='joined'))
    
    def toDict(self):
        return{
            'id': self.communityId,
            'name': self.name,
            'gameId': self.gameId,
           'users': [user.toDict() for user in self.Users]
        }

    