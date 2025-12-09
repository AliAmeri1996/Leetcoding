import sys
import math


# Line 1: The number nbitems of integers to sort.
# Line 2: nbitems space-separated integers.
# Output
# The nbitems properly sorted integers separated by a space.
# Constraints
# All given integers are positive and have a different count of '1's.

nbitems = int(input("Enter the number of items: "))  # Reads the number of items
a = []

# Reads a line of input, splits it into parts, and converts each part into an integer
for i in input("Enter the numbers separated by spaces: ").split():
    item = int(i)
    a.append(item)

# Sort the list 'a' based on the binary representation of its elements
a.sort(key=lambda x: bin(x)[2:])

print(a)
"""This creates a function that takes the specified arguments and returns the result of the expression. 
For example, lambda x: x * 2 defines a function that doubles its input.

In the context of a.sort(key=lambda x: bin(x)[2:]),
 the lambda function is used as the key argument in the sort method. The key parameter specifies a function that is applied to 
 each element of the list before sorting; the list is then sorted based on the results of this 
 function. Here, lambda x: bin(x)[2:] converts each integer x to its binary representation as a string
 (excluding the '0b' prefix) and returns that string. 
 The sort method then arranges the original integers in ascending order based on these binary string representations."""




