
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Plant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    image = db.Column(db.String(255), nullable=False)
    price = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<Plant {self.name}>'
