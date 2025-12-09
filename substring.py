def count_substring(string, sub_string):
    a = list(map(str, string.split()))
    b= list(map(str, sub_string.split()))
    numb=0

    if b in a:
        numb+=1
        return numb
    
   
        
        
        
print(count_substring("ABCDCDC","DC"))