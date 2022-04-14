from werkzeug.security import check_password_hash, generate_password_hash
from App.database import db

class User(db.Model):
    userId = db.Column(db.Integer, primary_key=True)
    username =  db.Column(db.String, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    gameId =  db.Column(db.Integer, db.ForeignKey('community.communityId'), nullable=False)
    myGames = db.relationship('MyGame', backref=db.backref('myGame', lazy='joined'))
    # gamesPlayed = db.relationship('MyGame', backref='user', lazy=True, cascade="all, delete-orphan")

    def __init__(self, username, password):
        self.username = username
        self.set_password(password)

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

# given in MVC Flask template
# minor modification to suit students user class based on class diagram.