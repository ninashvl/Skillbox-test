from app import db
from datetime import datetime


class Kitiki(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    breed = db.Column(db.String(50))
    age = db.Column(db.Integer)
    description = db.Column(db.Text)
    image = db.Column(db.Text)
    created = db.Column(db.DateTime, default=datetime.now)

    def __repr__(self):
        return f'<Cat id: {self.id}, breed: {self.breed}>'


