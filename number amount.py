def find(k,n):
    c=0
    for i in n:
        if i==k:
             c+=1
    return c

k=2
n=[2,3,2,4,2,4,2]
print(find(k,n))