import sqlite3
from pathlib import Path
from datetime import datetime

DB_PATH = Path(__file__).parent / "database.db"


def get_connection():
    return sqlite3.connect(DB_PATH)


def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        tg_id INTEGER UNIQUE,
        username TEXT,
        first_name TEXT,
        purchases INTEGER DEFAULT 0,
        balance INTEGER DEFAULT 0
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS purchases (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        tg_id INTEGER,
        product_name TEXT,
        price INTEGER,
        date TEXT
    )
    """)

    conn.commit()
    conn.close()


def add_user(tg_id, username, first_name):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT OR IGNORE INTO users (tg_id, username, first_name)
    VALUES (?, ?, ?)
    """, (tg_id, username, first_name))

    conn.commit()
    conn.close()


def get_user(tg_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM users WHERE tg_id = ?",
        (tg_id,)
    )
    user = cursor.fetchone()

    conn.close()
    return user


def add_purchase(tg_id, product_name, price):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO purchases (tg_id, product_name, price, date)
    VALUES (?, ?, ?, ?)
    """, (
        tg_id,
        product_name,
        price,
        datetime.now().strftime("%d.%m.%Y %H:%M")
    ))

    cursor.execute("""
    UPDATE users
    SET purchases = purchases + 1
    WHERE tg_id = ?
    """, (tg_id,))

    conn.commit()
    conn.close()


def get_purchases(tg_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT product_name, price, date
    FROM purchases
    WHERE tg_id = ?
    ORDER BY id DESC
    """, (tg_id,))

    result = cursor.fetchall()
    conn.close()
    return result
