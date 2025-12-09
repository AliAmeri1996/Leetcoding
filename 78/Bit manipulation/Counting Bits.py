def binary(n):
    l=[]
    for i in range(0,n+1):
        count=0
        while i:
            i &=(i-1) # this is for counting the 1s
            # in a matrix
            count+=1
        l.append(count)  
    return l

print(binary(4))

