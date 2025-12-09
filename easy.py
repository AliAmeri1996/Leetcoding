import sys
import math



count = int(input())
output=0
for i in input().split():
    number = int(i)
    if number%2==0:
        output+=number
    else:
        output*=number




print(output)