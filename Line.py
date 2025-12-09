import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

xa, xb, ya, yb = [int(i) for i in input().split()]
for i in range(1):
    x, y = [int(j) for j in input().split()]

a=(ya-yb/xa-xb)
b=(a*x -a*xa)+ya

print(y=a*x+b)




