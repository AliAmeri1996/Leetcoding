'On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time.'
' However, you can buy it then immediately sell it on the same day.'


'''Find and return the maximum profit you can achieve.'''

def max_profit(prices):
    profit = 0
    for i in range(1, len(prices)):
        if prices[i] > prices[i - 1]:# comparing the adjacent elements only
            profit += prices[i] - prices[i - 1]
    return profit


#O(n)


def maxProfit(prices):
    if not prices:
        return 0
    
    min_price = prices[0]# inittiliazing the min price.
    max_profit = 0
    
    for price in prices:
        min_price = min(min_price, price)      # Track lowest price so far
        profit = price - min_price              # Profit if selling today
        max_profit = max(max_profit, profit)    # Track best profit
    
    return max_profit




def maxProfit(prices):
    if not prices:
        return 0
    
    min_price = prices[0]
    max_profit = 0
    
    for price in prices:
        # Instead of: min_price = min(min_price, price)
        if price < min_price:
            min_price = price
        
        profit = price - min_price
        
        # Instead of: max_profit = max(max_profit, profit)
        if profit > max_profit:
            max_profit = profit
    
    return max_profit
