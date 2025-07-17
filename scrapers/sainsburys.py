import requests
from bs4 import BeautifulSoup
import streamlit as st

@st.cache_data(ttl=3600)  # Cache for 1 hour
def cached_search_sainsburys(query):
    from scrapers.sainsburys import search_sainsburys
    return search_sainsburys(query)

def search_sainsburys(query):
    url = f"https://www.sainsburys.co.uk/gol-ui/SearchResults/{query.replace(' ', '%20')}"
    headers = {"User-Agent": "Mozilla/5.0"}
    res = requests.get(url, headers=headers)

    if res.status_code != 200:
        return []

    soup = BeautifulSoup(res.text, "html.parser")
    products = []

    for item in soup.select(".pt-grid-item"):
        try:
            name = item.select_one(".pt__link").text.strip()
            price_text = item.select_one(".pt__price").text.strip()
            price = float(price_text.replace("£", "").split()[0])
            link = "https://www.sainsburys.co.uk" + item.select_one("a")["href"]
            image = item.select_one("img")["src"]
            products.append({
                "supermarket": "Sainsbury’s",
                "name": name,
                "price": price,
                "url": link,
                "image": image
            })
        except:
            continue

    return products
