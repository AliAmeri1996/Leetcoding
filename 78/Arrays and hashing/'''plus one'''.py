'''plus one'''
'''You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer.'''


def plusone(digits):
    for i in range(len(digits)-1,-1,-1):
        if digits[i]<9:
            digits[i]+=1
            return digits
        digits[i]=0

    return [1] + digits #[1] + [0,0,0] we're using this line if all the digits were 9s


print(plusone([4,3,2,1]))

#return [1] + digits
'''Example: [9,9,9] → should become [1,0,0,0]

Inside the loop we turn every 9 into 0, but we still need to handle the carry that’s left over.
[1] is a list with a single element 1
is only needed when the number is made up of all 9s (every digit is 9).'''

'''If that last element is less than 9, we add 1 and return immediately → ✅ only the last element gets checked.

If the last element is 9, we set it to 0 and keep moving left → so now the second-last element is checked, and maybe the third-last, etc.'''

