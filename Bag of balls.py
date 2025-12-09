import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
c = int(input())
dictColor = {}
for i in range(c):
    s = input().split(",")
    dictColor[s[0]] = int(s[1]) #s[0] is the key.
    #s[1] will be the second element(value), which is converted into an integer.
t = input().split(",")#Splits the input string into a list using , as the separator.

res = 1
for color in t:
    res *= dictColor[color]/n

if sum(dictColor.values()) != n:
    print("Error")
else:
    print("{:.4f}".format(round(res, 4)))