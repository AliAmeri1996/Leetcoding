'''Given an array and an integer k, find the contiguous subarray of length k that has the maximum average value.'''


def best_total_prices(prices,k):
    maxtotal=0
    for i in range(len(prices)-k+1):# this is basically stops the range to go out of the length of the subarray
        total=sum(prices[i:i+k])# this is the way of sliding, from the index of i to i+k
        maxtotal=max(maxtotal,total)
    return maxtotal



print(best_total_prices(prices = [1, 12, -5, -6, 50, 3],k = 4))