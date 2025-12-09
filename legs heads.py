import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

heads, legs = [int(i) for i in input("tell me about heads and legs").split()]

for i in range(0,heads):
    if i*4 + (heads-i)*2 == legs:
        print(heads-i,i)