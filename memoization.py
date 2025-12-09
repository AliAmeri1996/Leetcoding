memo = {}#This is a dictionary (memo) that stores previously calculated Fibonacci values.
def fibonacci_memo(n):
    if n in memo:#Checks if the Fibonacci number for n is already computed.
        return memo[n]#If it exists in the memo dictionary, return the stored value instead of recalculating.
    if n == 0:
        return 0
    if n == 1:
        return 1
    memo[n] = fibonacci_memo(n-1) + fibonacci_memo(n-2)#If n is not in memo, the function recursively computes 
    #Fibonacci numbers for n-1 and n-2.
    #The result is stored in memo[n] to avoid duplicate calculations in future calls.
    return memo[n]
print(fibonacci_memo(10))