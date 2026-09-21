from flask import Flask, jsonify
import mysql.connector
import os

app = Flask(__name__)

def get_db():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST", "mysql"),
        user=os.getenv("DB_USER", "root"),
        password=os.getenv("DB_PASSWORD", "root"),
        database=os.getenv("DB_NAME", "appdb")
    )

@app.route("/")
def home():
    return jsonify({"message": "Two-tier backend is running"})

@app.route("/db")
def database():
    try:
        db = get_db()
        db.close()
        return jsonify({"database": "MySQL connected"})
    except Exception as e:
        return jsonify({"database": "Connection failed", "error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
