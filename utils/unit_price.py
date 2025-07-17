import re

def extract_quantity(name):
    """
    Extracts quantity and unit from product name, returns (value in base unit, unit type)
    """
    match = re.search(r"([\d\.]+)\s?(ml|l|cl|g|kg)", name.lower())
    if not match:
        return None, None

    quantity = float(match.group(1))
    unit = match.group(2)

    # Convert all volumes to litres, weights to kg
    if unit == "ml":
        return quantity / 1000, "L"
    elif unit == "cl":
        return quantity / 100, "L"
    elif unit == "l":
        return quantity, "L"
    elif unit == "g":
        return quantity / 1000, "kg"
    elif unit == "kg":
        return quantity, "kg"
    else:
        return None, None

def calculate_unit_price(price, quantity):
    if quantity and quantity > 0:
        return round(price / quantity, 2)
    return None
