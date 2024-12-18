from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Race(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    season = db.Column(db.String(4))
    round = db.Column(db.Integer)
    race_name = db.Column(db.String(100))
    circuit_name= db.Column(db.String(100))
    results = db.relationship('Result', backref='race', lazy='select')

class Driver (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    nationality = db.Column(db.String(50))
    results = db.relationship('Result', backref='driver', lazy='select')

class Result(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    position = db.Column(db.Integer)
    time = db.Column(db.String(20))
    race_id = db.Column(db.Integer, db.ForeignKey('race.id'))
    driver_id = db.Column(db.Integer, db.ForeignKey('driver.id'))