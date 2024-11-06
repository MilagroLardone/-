from . import db

class Photo(db.model):
    __tablename__ = 'photo'
    id = db.Column(db.Interger, primarykey = True)
    title = db.Column(db.String(50), nullable = False)
    description = db.Column(db.String(200), NotNull = True)
    image =  db.Column(db.String(200), NotNull = False)

    