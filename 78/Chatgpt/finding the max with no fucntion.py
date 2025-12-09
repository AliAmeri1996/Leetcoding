def maximum(n):
    maxi=n[0]
    for i in range(1,len(n)):
        if n[i]>maxi:
            maxi=n[i]

    return maxi
    
print(maximum([1,2,4,7,9]))