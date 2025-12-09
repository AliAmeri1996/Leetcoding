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


