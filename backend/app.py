from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)

DB_NAME = "male.db"

def get_db():
    return sqlite3.connect(DB_NAME)

def create_table():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS male (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER NOT NULL,
            work TEXT NOT NULL,
            phone TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

create_table()

@app.route("/")
def home():
    return "Backend is running!"

@app.route("/register", methods=["POST"])
def register():
    data = request.json

    name = data.get("name")
    age = data.get("age")
    work = data.get("work")
    phone = data.get("phone")

    if not all([name, age, work, phone]):
        return jsonify({"message": "All fields are required"}), 400

    conn = get_db()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO male (name, age, work, phone) VALUES (?, ?, ?, ?)",
        (name, age, work, phone)
    )
    conn.commit()
    conn.close()

    return jsonify({"message": "Saved successfully!"})

@app.route("/males", methods=["GET"])
def get_males():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, age, work, phone FROM male")
    rows = cursor.fetchall()
    conn.close()

    males = []
    for row in rows:
        males.append({
            "id": row[0],
            "name": row[1],
            "age": row[2],
            "work": row[3],
            "phone": row[4]
        })

    return jsonify(males)

if __name__ == "__main__":
    app.run(debug=True)