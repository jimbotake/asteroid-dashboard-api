from flask import Flask, request, jsonify, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
CORS(app)  # aktifkan CORS untuk semua route

# Database config
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")

app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Asteroid(db.Model):
    __tablename__ = 'asteroids'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    size_km = db.Column(db.Float, nullable=False)
    hazardous = db.Column(db.Boolean, nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "size_km": self.size_km,
            "hazardous": self.hazardous
        }

@app.route('/')
def serve_dashboard():
    return send_from_directory('.', 'dashboard.html')  # file HTML di folder sama dengan app.py

@app.route('/asteroids', methods=['GET'])
def get_asteroids():
    data = Asteroid.query.all()
    return jsonify([a.to_dict() for a in data])

@app.route('/asteroids/<int:id>', methods=['GET'])
def get_asteroid(id):
    a = Asteroid.query.get(id)
    if a:
        return jsonify(a.to_dict())
    return jsonify({"error": "Asteroid tidak ditemukan"}), 404

@app.route('/asteroids', methods=['POST'])
def add_asteroid():
    data = request.get_json()
    if not data or not all(k in data for k in ("name", "size_km", "hazardous")):
        return jsonify({"error": "Data tidak lengkap"}), 400
    new = Asteroid(name=data["name"], size_km=data["size_km"], hazardous=data["hazardous"])
    db.session.add(new)
    db.session.commit()
    return jsonify(new.to_dict()), 201

@app.route('/asteroids/<int:id>', methods=['DELETE'])
def delete_asteroid(id):
    a = Asteroid.query.get(id)
    if a:
        db.session.delete(a)
        db.session.commit()
        return jsonify({"message": f"Asteroid ID {id} dihapus"})
    return jsonify({"error": "Asteroid tidak ditemukan"}), 404

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
