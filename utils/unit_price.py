import re

def extract_quantity(name):
    """
    Extracts quantity from product name. Handles single units and multipacks.
    Returns: (total_quantity, unit_type)
    """
    name = name.lower()
    
    # First handle multipack like "6 x 330ml" or "4x500g"
    multipack_match = re.search(r"(\d+)\s*[xX×]\s*([\d\.]+)\s?(ml|l|cl|g|kg)", name)
    if multipack_match:
        count = int(multipack_match.group(1))
        qty = float(multipack_match.group(2))
        unit = multipack_match.group(3)
    else:
        # Fallback: single quantity
        match = re.search(r"([\d\.]+)\s?(ml|l|cl|g|kg)", name)
        if not match:
            return None, None
        count = 1
        qty = float(match.group(1))
        unit = match.group(2)

    # Normalize to base unit
    if unit == "ml":
        total = count * qty / 1000
        return total, "L"
    elif unit == "cl":
        total = count * qty / 100
        return total, "L"
    elif unit == "l":
        return count * qty, "L"
    elif unit == "g":
        return count * qty / 1000, "kg"
    elif unit == "kg":
        return count * qty, "kg"

    return None, None
