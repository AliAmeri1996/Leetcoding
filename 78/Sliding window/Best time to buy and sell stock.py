def max_profit(prices):
    l = 0  #supposed to track the cheapest day to buy so far, this is the pointer to find the buying day.              
    max_prof = 0
    for r in range(1, len(prices)):   # sell pointer, todays price
        if prices[r] < prices[l]:#If today’s price (prices[r]) is smaller than our current buy price (prices[l])
            l = r # you are literally moving the l pointer (buy pointer) to the right
        else:
            max_prof = max(max_prof, prices[r] - prices[l])
    return max_prof


print(max_profit([10,1,5,6,7,1]))

'''l = the buy day pointer
   r = the sell day pointer'''

#if prices[r] < prices[l] l = r :
'''l = 0 → we’re considering buying on day 0 (first element in prices).
r = 1 → we’re considering selling on day 1 (second element).
it basically means compare the two next to each other values until the right one is bigger than the left line 
l always referes to the smalles day so far seen and r is the current day
when l is bigger than r, it also keeps going to the right
when else is triggered 
'''


# l is the buying point
# r is the selling point