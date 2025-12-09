def find_max(prices):
    max_price = float('-inf')  # Start with the smallest possible number
    for i in prices:
        if i > max_price:
            max_price = i
    return max_price