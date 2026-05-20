from flask import Flask, request, jsonify
import sqlite3
from datetime import datetime

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect("bank.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS accounts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            balance REAL NOT NULL
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            from_account INTEGER,
            to_account INTEGER,
            amount REAL NOT NULL,
            created_at TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()

@app.route("/")
def home():
    return "AussieBankOps is running"

@app.route("/health")
def health():
    return jsonify({"status": "healthy"})

@app.route("/account/create", methods=["POST"])
def create_account():
    data = request.get_json()

    name = data["name"]
    balance = data["balance"]

    conn = sqlite3.connect("bank.db")
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO accounts (name, balance) VALUES (?, ?)",
        (name, balance)
    )
    conn.commit()
    conn.close()

    return jsonify({"message": "Account created successfully"})

@app.route("/transfer", methods=["POST"])
def transfer():
    data = request.get_json()

    from_account = data["from_account"]
    to_account = data["to_account"]
    amount = data["amount"]

    conn = sqlite3.connect("bank.db")
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE accounts SET balance = balance - ? WHERE id = ?",
        (amount, from_account)
    )

    cursor.execute(
        "UPDATE accounts SET balance = balance + ? WHERE id = ?",
        (amount, to_account)
    )

    cursor.execute(
        "INSERT INTO transactions (from_account, to_account, amount, created_at) VALUES (?, ?, ?, ?)",
        (from_account, to_account, amount, datetime.now().isoformat())
    )

    conn.commit()
    conn.close()

    return jsonify({"message": "Transfer successful"})

if __name__ == "__main__":
    init_db()
    app.run(debug=True)