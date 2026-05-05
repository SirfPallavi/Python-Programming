def calculate_total(items, tax_rate):
    # Validate tax rate
    if tax_rate < 0 or tax_rate > 1:
        raise ValueError("Invalid tax rate")

    total = 0

    for price in items:
        # Validate item price
        if price < 0:
            raise ValueError("Price cannot be negative")
        total += price

    # Add tax
    return total + (total * tax_rate)
