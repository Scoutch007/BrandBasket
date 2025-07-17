import streamlit as st
from scrapers.tesco import search_tesco
from scrapers.asda import search_asda
from scrapers.sainsburys import search_sainsburys
from scrapers.morrisons import search_morrisons
from utils.matcher import group_similar_products

st.title("🛒 UK Supermarket Price Comparison")
query = st.text_input("Search for a branded product:", "Coca-Cola 1.75L")

# After user enters query:
results = (
    search_tesco(query)
    + search_asda(query)
    + search_sainsburys(query)
    + search_morrisons(query)
)

with st.sidebar:
    st.header("🔍 Filters")
    selected_supermarkets = st.multiselect(
        "Select Supermarkets", 
        ["Tesco", "Asda", "Sainsbury’s", "Morrisons"], 
        default=["Tesco", "Asda", "Sainsbury’s", "Morrisons"]
    )
    price_min, price_max = st.slider("Price Range (£)", 0.0, 10.0, (0.0, 10.0), step=0.1)

if results:
    filtered_results = [
    item for item in results
    if item["supermarket"] in selected_supermarkets
    and price_min <= item["price"] <= price_max
    ]
    grouped_results = group_similar_products(filtered_results)

    for group in grouped_results:
        st.markdown("### 🧾 Matched Product Group")
        for result in sorted(group, key=lambda x: x['price']):
            st.subheader(result["supermarket"])
            if "image" in result:
                st.image(result["image"], width=120)
            st.write(f"**{result['name']}**")
            st.write(f"💷 £{result['price']:.2f}")
            st.markdown(f"[🔗 View Product]({result['url']})")
            st.markdown("---")
