'''Move Zeroes'''

def movezeros(digits):
    j=0 # this way, we have created an empty slot at the first element
    for i in range(len(digits)):
        if digits[i]!=0:
            digits[j]=digits[i]# so when the digit is not zero, it goes into the slot of digits[j] which is empty
            j+=1 #this basically means whenever, you moved something to the left slot,add one to j and then next time

    for k in range(j,len(digits)):
        digits[k]=0

    return digits
        
            
    
'''two-pointer technique!'''
'''O(n)'''
   