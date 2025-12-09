'''Reverse String'''

def reverseString(s):

        left=0
        right = len(s) - 1
        while left < right:   #boundary condition
            # swap characters
            s[left], s[right] = s[right], s[left]
            # move pointers
            left += 1
            right -= 1
        return s


print(reverseString(["h","e","l","l","o"]))
'''Two-Pointer Technique'''

