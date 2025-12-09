def hammingWeight(n):
    count = 0
    while n:# this runs as long as n is not 0
        n &= (n - 1)  
        count += 1
    return count


print(hammingWeight(0b00000000000000000000000000010111))

#In Python, while n: is shorthand for while n != 0:
#n &= (n - 1) is shorthand for:
#n = n & (n - 1)
#This does a bitwise AND between n and n - 1
#It clears (removes) the rightmost 1 bit in n