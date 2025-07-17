import requests
from bs4 import BeautifulSoup

def search_morrisons(query):
    url = f"https://groceries.morrisons.com/search?entry={query.replace(' ', '+')}"
    headers = {"User-Agent": "Mozilla/5.0"}
    res = requests.get(url, headers=headers)

    if res.status_code != 200:
        return []

    soup = BeautifulSoup(res.text, "html.parser")
    products = []

    for item in soup.select("li.fop-item"):
        try:
            name = item.select_one(".fop-title").text.strip()
            price_text = item.select_one(".fop-price").text.strip().replace("£", "")
            price = float(price_text.split()[0])
            link = "https://groceries.morrisons.com" + item.find("a")["href"]
            image = item.find("img")["src"]
            products.append({
                "supermarket": "Morrisons",
                "name": name,
                "price": price,
                "url": link,
                "image": image
            })
        except:
            continue

    return products
