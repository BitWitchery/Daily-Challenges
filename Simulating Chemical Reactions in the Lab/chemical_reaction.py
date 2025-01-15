def simulate_reaction(elements, quantities):
    # Write code here 
    if not elements or not quantities or len(elements) != len(quantities):
        raise ValueError("Elements and quantities must be non-empty lists of the same length.")

    # Combine the first two elements if both exist and have non-zero quantities
    if len(elements) >= 2 and quantities[0] > 0 and quantities[1] > 0:
        qquantities[2] *= 2

    # Reverse the order of elements and quantities
    elements.reverse()
    quantities.reverse()

    # Remove any elements with zero quantity
    final_elements = [f"{elements[i]}{quantities[i]}" for i in range(len(elements)) if quantities[i] > 0]

    return final_elementsuantities[0] += quantities[1]  # Add quantities
        elements.pop(1)  # Remove the second element
        quantities.pop(1)  # Remove the second quantity

    # Double the quantity of the third element if it exists
    if len(quantities) >= 3:
        

