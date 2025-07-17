import requests
from bs4 import BeautifulSoup

def search_asda(query):
    url = f"https://groceries.asda.com/search/{query.replace(' ', '%20')}"
    headers = {"User-Agent": "Mozilla/5.0"}
    res = requests.get(url, headers=headers)

    if res.status_code != 200:
        return []

    soup = BeautifulSoup(res.text, "html.parser")
    results = []

    for item in soup.select(".co-product"):
        try:
            name = item.select_one(".co-product__title").text.strip()
            price_text = item.select_one(".co-product__price").text.strip().replace("£", "")
            price = float(price_text.split("/")[0].strip())  # remove per L or kg if needed
            link = "https://groceries.asda.com" + item.find("a")["href"]
            results.append({
                "supermarket": "Asda",
                "name": name,
                "price": price,
                "url": link
            })
        except:
            continue

    return results
