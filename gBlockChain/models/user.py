from gBlockChain.lib.database import db, Model, Column, relationship, reference_col

class User(Model):
    __tablename__ = 'user'
    id = Column(db.Integer, primary_key=True, autoincrement=True, unique=True )
    name = Column(db.String(64), primary_key=True, index=True, unique=True)
    email = Column(db.String(64), unique=False, nullable=False)
    user_id = Column(db.String(32), unique=False)
    name = Column(db.Unicode(32))
    state = Column(db.String(32), default="")
    is_admin = Column(db.Boolean, default=False)
    avatar_url = Column(db.String(128), default="")
    web_url = Column(db.String(128), default="")
    identities = Column(db.Text, default="")

    def __init__(self, name):
        self.name = name
 
    def __repr__(self):
        return '<User %r>' % self.name

