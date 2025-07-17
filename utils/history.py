import os
import pandas as pd
from datetime import datetime

HISTORY_FILE = "data/price_history.csv"

def load_price_history():
    if os.path.exists(HISTORY_FILE):
        return pd.read_csv(HISTORY_FILE)
    return pd.DataFrame(columns=["timestamp", "product_name", "supermarket", "price", "url"])

def save_price_entry(name, supermarket, price, url):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entry = pd.DataFrame([{
        "timestamp": timestamp,
        "product_name": name,
        "supermarket": supermarket,
        "price": price,
        "url": url
    }])

    df = load_price_history()
    df = pd.concat([df, entry], ignore_index=True)
    df.to_csv(HISTORY_FILE, index=False)

def get_history_for_url(url):
    df = load_price_history()
    return df[df["url"] == url].sort_values("timestamp", ascending=False)
