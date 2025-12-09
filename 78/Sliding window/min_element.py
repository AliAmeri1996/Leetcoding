def max(prices):
    min_price=float('inf')
    for i in prices:
        if i<min_price:
            min_price=i
    return min_price

prices = [10, 1, 5, 6, 7, 2]
print(max(prices))