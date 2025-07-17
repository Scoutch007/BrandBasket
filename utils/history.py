import sqlite3
from datetime import datetime
import pandas as pd
import os

DB_PATH = "data/price_history.db"

def init_db():
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS price_history (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp TEXT,
                product_name TEXT,
                supermarket TEXT,
                price REAL,
                url TEXT
            )
        """)

def save_price_entry(name, supermarket, price, url):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute("""
            INSERT INTO price_history (timestamp, product_name, supermarket, price, url)
            VALUES (?, ?, ?, ?, ?)
        """, (timestamp, name, supermarket, price, url))

def get_history_for_url(url):
    with sqlite3.connect(DB_PATH) as conn:
        df = pd.read_sql("SELECT * FROM price_history WHERE url = ? ORDER BY timestamp DESC", conn, params=(url,))
    return df
