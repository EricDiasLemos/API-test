import os
from flask import Flask, jsonify
from db import get_db, close_db

app = Flask(__name__)
app.teardown_appcontext(close_db)

@app.route("/")
def home():
    return "API funcionando"

@app.route("/create-table")
def create_table():
    conn = get_db()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            name TEXT NOT NULL
        );
    """)
    conn.commit()
    return jsonify({"status": "table created"})

@app.route("/add-user/<name>")
def add_user(name):
    conn = get_db()
    cur = conn.cursor()
    cur.execute("INSERT INTO users (name) VALUES (%s)", (name,))
    conn.commit()
    return jsonify({"status": "user added"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8081)))
