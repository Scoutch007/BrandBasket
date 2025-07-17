import streamlit as st
from scrapers.tesco import search_tesco
from scrapers.asda import search_asda
from scrapers.sainsburys import search_sainsburys
from scrapers.morrisons import search_morrisons
from utils.matcher import group_similar_products
from utils.unit_price import extract_quantity, calculate_unit_price
from utils.history import save_price_entry, get_history_for_url
from utils.exporter import generate_csv, generate_pdf
from utils.history import init_db

init_db()

st.title("🛒 UK Supermarket Price Comparison")
query = st.text_input("Search for a branded product:", "Coca-Cola 1.75L")

# After user enters query:
results = (
    cached_search_tesco(query)
    + cached_search_asda(query)
    + cached_search_sainsburys(query)
    + cached_search_morrisons(query)
)

with st.sidebar:
    st.header("🔍 Filters")
    selected_supermarkets = st.multiselect(
        "Select Supermarkets", 
        ["Tesco", "Asda", "Sainsbury’s", "Morrisons"], 
        default=["Tesco", "Asda", "Sainsbury’s", "Morrisons"]
    )
    unit_price_min, unit_price_max = st.slider("Unit Price Range (£/L or £/kg)", 0.0, 10.0, (0.0, 10.0), step=0.1)

if results:
    filtered_results = [
    item for item in results
    if item["supermarket"] in selected_supermarkets
    and price_min <= item["price"] <= price_max
    and (
        item["unit_price"] is None or 
        unit_price_min <= item["unit_price"] <= unit_price_max
    )
]

    # Enhance each product with quantity/unit and unit price
for item in results:
    save_price_entry(item["name"], item["supermarket"], item["price"], item["url"])
    qty, unit_type = extract_quantity(item["name"])
    item["quantity"] = qty
    item["unit_type"] = unit_type
    item["unit_price"] = calculate_unit_price(item["price"], qty)
    
    grouped_results = group_similar_products(filtered_results)
    history = get_history_for_url(result["url"])

    for group in grouped_results:
        st.markdown("### 🧾 Matched Product Group")
        for result in sorted(group, key=lambda x: x.get('unit_price') or float('inf')):
            st.subheader(result["supermarket"])
            if "image" in result:
                st.image(result["image"], width=120)
            st.write(f"**{result['name']}**")
            st.write(f"💷 £{result['price']:.2f}")
            if result["unit_price"]:
                st.write(f"📏 Unit Price: £{result['unit_price']:.2f} per {result['unit_type']}")
            st.markdown(f"[🔗 View Product]({result['url']})")
            if not history.empty:
                st.markdown("🕒 **Price History (last 5 entries)**")
                st.dataframe(history.head(5)[["timestamp", "price"]])
            st.markdown("---")
    if filtered_results:
    st.download_button("⬇️ Export as CSV", generate_csv(filtered_results), "comparison.csv", "text/csv")
    st.download_button("⬇️ Export as PDF", generate_pdf(filtered_results), "comparison.pdf", "application/pdf")
