from gBlockChain.lib.database import db, Model, Column, relationship, reference_col

class User(Model):
    id = Column(db.Integer, primary_key=True)
    name = Column(db.Unicode, unique=True)
    birth_date = Column(db.Date)
