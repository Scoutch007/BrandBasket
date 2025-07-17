import streamlit as st
from scrapers.tesco import search_tesco
from scrapers.asda import search_asda
from scrapers.sainsburys import search_sainsburys
from scrapers.morrisons import search_morrisons

st.title("🛒 UK Supermarket Price Comparison")
query = st.text_input("Search for a branded product:", "Coca-Cola 1.75L")

# After user enters query:
results = (
    search_tesco(query)
    + search_asda(query)
    + search_sainsburys(query)
    + search_morrisons(query)
)

if not results:
    st.warning("No results found.")
else:
    for result in sorted(results, key=lambda x: x["price"]):
        st.subheader(result["supermarket"])
        if "image" in result:
            st.image(result["image"], width=120)
        st.write(f"**{result['name']}**")
        st.write(f"💷 £{result['price']:.2f}")
        st.markdown(f"[🔗 View Product]({result['url']})")
        st.markdown("---")
