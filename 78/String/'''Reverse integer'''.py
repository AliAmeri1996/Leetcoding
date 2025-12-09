'''Reverse integer'''
def reverse(x: int) -> int:
    
    INT_MIN=-2**31
    INT_MAX =2**31 - 1  
    
    if x < 0:
        rev = -int(str(-x)[::-1])   # reverse digits of positive, then add back minus
    else:
        rev = int(str(x)[::-1])
    
    # check 32-bit signed range
    if rev < INT_MIN or rev > INT_MAX:
        return 0
    return rev
