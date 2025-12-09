def missing_number(n):
    l=[]
    s=[]
    a=max(n)
    for g in range(0,a+1):
        l.append(g)
    for i in l:
        if i not in n:
            s.append(i)
    return s
            
       

   
print(missing_number([1,2,3,5]))