from flask import Flask, jsonify, request
import sqlite3

app = Flask(__name__)


def get_db_connection():
    connection = sqlite3.connect("expense_tracker.db")
    connection.row_factory = sqlite3.Row
    return connection


@app.route("/")
def home():
    return "Expense Tracker Backend is running!"


@app.route("/api/test")
def test():
    return jsonify({
        "message": "API is working",
        "status": "success"
    })

@app.route("/register", methods=["POST"])
def register():
    data = request.get_json()

    name = data["name"]
    email = data["email"]
    password = data["password"]

    connection = get_db_connection()

    connection.execute(
        "INSERT INTO users (name, email, password) VALUES (?, ?, ?)",
        (name, email, password)
    )

    connection.commit()
    connection.close()

    return jsonify({
        "message": "User registered successfully"
    })

if __name__ == "__main__":
    app.run(debug=True)