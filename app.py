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

if results:
    grouped_results = group_similar_products(results)

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
