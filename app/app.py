from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import os
import time
import psycopg2

app = Flask(__name__)

DB_URL = os.getenv("DATABASE_URL", "postgresql://user:1234@db:5432/mydb")
app.config["SQLALCHEMY_DATABASE_URI"] = DB_URL
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

def wait_for_db():
    while True:
        try:
            conn = psycopg2.connect(DB_URL)
            conn.close()
            print("Database is ready!")
            break
        except psycopg2.OperationalError:
            print("Database not yet ready, waiting...")
            time.sleep(2)

wait_for_db()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

@app.route("/users", methods=["POST"])
def add_user():
    data = request.json
    name = data.get("name")
    if not name:
        return jsonify({"error": "Name is required"}), 400
    
    new_user = User(name=data["name"])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User added", "id": new_user.id}), 201

@app.route("/users", methods=["GET"])
def get_users():
    users = User.query.all()
    return jsonify([{"id": u.id, "name": u.name} for u in users])

if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    app.run(host="0.0.0.0", port=8000)