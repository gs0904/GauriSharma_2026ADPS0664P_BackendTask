from flask import Flask, jsonify

app = Flask(__name__)


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