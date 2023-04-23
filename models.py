
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    password = db.db.Column(db.String(20), nullable=False)
    age = db.Column(db.Integer)

    def serialize(self):
        return {
            "username": self.username,
            "id": self.id,
            "age": self.age
        }

class Favorite(db.Model):
    __tablename__ = 'favorite'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.Integer, db.ForeignKey('user.id'))
    character_id = db.Column(db.Integer, db.ForeignKey('character.id'))
    name = db.Column(db.String(50), nullable=False)
  

    def serialize(self):
        return {
            "id": self.id,
            "name" : self.name,
            "username" : self.username,
            "character_id" : self.character_id
        }

class Character(db.Model):
    __tablename__ = 'character'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    actor = db.Column(db.String(50), nullable=False)
    house = db.Column(db.String(50), nullable=False)
    date_of_birth = db.Column(db.String(50))
    patronus = db.Column(db.String(50))
    half_blood = db.Column(db.String(50))
    favorite_username = db.Column(db.Integer, db.ForeignKey('favorite.username'))

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "actor": self.actor,
            "house": self.house,
            "date_of_birth": self.date_of_birth,
            "patronus": self.patronus,
            "half_blood": self.half_blood,
            "favorite_username": self.favorite_username,
        }
