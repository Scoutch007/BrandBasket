import streamlit as st
from scrapers.tesco import search_tesco
from scrapers.asda import search_asda

st.title("🛒 UK Supermarket Price Comparison")
query = st.text_input("Search for a branded product:", "Coca-Cola 1.75L")

if query:
    st.write("🔍 Searching Tesco and Asda...")
    
    tesco_results = search_tesco(query)
    asda_results = search_asda(query)
    
    all_results = tesco_results + asda_results
    if not all_results:
        st.warning("No results found.")
    else:
        for result in sorted(all_results, key=lambda x: x['price']):
            st.subheader(result["supermarket"])
            st.write(f"**{result['name']}**")
            st.write(f"💷 £{result['price']:.2f}")
            st.markdown(f"[View Product]({result['url']})")
            st.markdown("---")
