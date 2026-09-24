from flask import Flask, jsonify
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


if __name__ == "__main__":
    app.run(debug=True)