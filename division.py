#You are given N elements, your task is to determine the number of elements divisible by K
#Input
#Line 1: An integer N, representing the number of elements.
#Line 2: An integer K, representing the divisor.
#Next N lines: Each containing one integer, representing an element from the list.
#Output
#Print the number of elements divisible by K.





# Read input values
N = int(input("Enter the number of elements: "))
K = int(input("Enter the divisor: "))

count = 0

# Loop through the next N lines to read elements
for _ in range(N):
    element = int(input())# this is for putting the actual elements which has to be done in a perpendicular line
    if element % K == 0:
        count += 1


print(count)