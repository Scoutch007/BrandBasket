import streamlit as st

# Supported supermarkets with their delivery URLs
SUPPORTED_SUPERMARKETS = {
    "Tesco": "https://www.tesco.com/groceries/en-GB/slots",
    "ASDA": "https://groceries.asda.com/slot-booking",
    "Sainsbury's": "https://www.sainsburys.co.uk/gol-ui/Login",
    "Morrisons": "https://groceries.morrisons.com/delivery",
    "Waitrose": "https://www.waitrose.com/ecom/shop/browse/groceries"
}

# Mock postcode coverage mapping
MOCK_COVERAGE = {
    "E1": ["Tesco", "ASDA", "Sainsbury's"],
    "SW1": ["Waitrose", "Tesco"],
    "LS1": ["Morrisons", "ASDA"],
    "M1": ["ASDA", "Tesco", "Sainsbury's", "Morrisons"]
}

def check_postcode_coverage(postcode):
    """
    Mock function to determine delivery availability by area code.
    """
    area = postcode.upper().split(" ")[0]
    return MOCK_COVERAGE.get(area, [])

def get_delivery_page(supermarket):
    """
    Returns the official delivery URL for a given supermarket.
    """
    return SUPPORTED_SUPERMARKETS.get(supermarket)

def show_delivery_ui():
    """
    Streamlit UI to check delivery availability and provide links.
    """
    st.subheader("🚚 Check Delivery Availability")
    postcode = st.text_input("Enter your postcode:", max_chars=8)

    if postcode:
        covered = check_postcode_coverage(postcode)
        if covered:
            st.success(f"The following supermarkets deliver to **{postcode.upper()}**:")
            for sm in covered:
                url = get_delivery_page(sm)
                st.markdown(f"- [{sm} Delivery Page]({url})")
        else:
            st.warning(f"Sorry, we don't have delivery info for **{postcode.upper()}**.")
