from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///plants.db'  # Change the URI as needed
db = SQLAlchemy(app)

# Replace this with the actual model definition in models.py
class Plant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    image = db.Column(db.String(255), nullable=False)
    price = db.Column(db.Float, nullable=False)

# Routes

@app.route('/plants', methods=['GET'])
def get_plants():
    plants = Plant.query.all()
    plant_list = [{"id": plant.id, "name": plant.name, "image": plant.image, "price": plant.price} for plant in plants]
    return jsonify(plant_list)

@app.route('/plants/<int:plant_id>', methods=['GET'])
def get_plant(plant_id):
    plant = Plant.query.get_or_404(plant_id)
    return jsonify({"id": plant.id, "name": plant.name, "image": plant.image, "price": plant.price})

@app.route('/plants', methods=['POST'])
def create_plant():
    data = request.get_json()

    new_plant = Plant(
        name=data['name'],
        image=data['image'],
        price=data['price']
    )

    db.session.add(new_plant)
    db.session.commit()

    return jsonify({"id": new_plant.id, "name": new_plant.name, "image": new_plant.image, "price": new_plant.price}), 201

if __name__ == '__main__':
    db.create_all()
    app.run(port=5555,debug=True)

