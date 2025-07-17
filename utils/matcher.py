from rapidfuzz import process, fuzz

def group_similar_products(products, threshold=85):
    grouped = []
    used = set()

    for i, item in enumerate(products):
        if i in used:
            continue

        group = [item]
        used.add(i)

        for j in range(i+1, len(products)):
            if j in used:
                continue
            score = fuzz.token_sort_ratio(item["name"], products[j]["name"])
            if score >= threshold:
                group.append(products[j])
                used.add(j)

        grouped.append(group)

    return grouped
