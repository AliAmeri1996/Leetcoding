import sys
import math


a=[]
h=0
n = int(input())
s = list(map(int, input().split()))
if n!=len(s):
    raise ValueError
for i in s:
    a.append(i**2)
for t in a:
    h+=t
print(h)


 

   


    

    

    



