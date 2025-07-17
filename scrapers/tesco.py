import requests
from bs4 import BeautifulSoup

def search_tesco(query):
    url = f"https://www.tesco.com/groceries/en-GB/search?query={query.replace(' ', '%20')}"
    headers = {"User-Agent": "Mozilla/5.0"}
    res = requests.get(url, headers=headers)
    
    if res.status_code != 200:
        return []

    soup = BeautifulSoup(res.text, "html.parser")
    results = []
    
    for product in soup.select(".product-list--list-item"):
        try:
            name = product.select_one(".product-title__title").text.strip()
            price_text = product.select_one(".value").text.strip()
            price = float(price_text.replace("£", "").replace(",", ""))
            link = "https://www.tesco.com" + product.select_one("a")["href"]
            results.append({
                "supermarket": "Tesco",
                "name": name,
                "price": price,
                "url": link
            })
        except:
            continue

    return results
