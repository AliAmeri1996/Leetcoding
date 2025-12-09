def portfolio(n):
    max_val = max(n)
    min_val = min(n)
    
    max_idx = n.index(max_val)
    min_idx = n.index(min_val)
    
    # Swap the values
    n[max_idx], n[min_idx] = n[min_idx], n[max_idx]
    
    return n

# Example
print(portfolio([4, 2, 9, 1, 5])) 