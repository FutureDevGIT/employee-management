import sqlite3
from flask import jsonify

DB_NAME = "employees.db"

def get_db_connection():
    try:
        conn = sqlite3.connect(DB_NAME)
        conn.row_factory = sqlite3.Row
        return conn
    except Exception as e:
        return jsonify({"error": str(e)}), 500