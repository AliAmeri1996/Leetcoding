'''You are given a string s consisting of the following characters: '(', ')', '{', '}', '[' and ']'.
'''

def isValid( s: str) -> bool:
        stack = []
        bracket_map = {')': '(', '}': '{', ']': '['}

        for char in s:
              if char in bracket_map.values():
                   stack.append(char)# if char is an opening bracket, itll be pushed into the stack
              elif char in bracket_map:# this means it checks the first, left element of the dictioary
                   if not stack or stack[-1] != bracket_map[char]: # basically this gets the elemenet that not in the value
                       # and its the key, puts it in this bracket_map[char] code to find its value , if they're not the same, False, basically
                       # this checks whether the signs are of the same nature.
                       return False
                   stack.pop()
              else:
            # If the character is not a bracket (optional check)
                    return False

        return not stack


#if not stack or stack[-1] != bracket_map[char]:
'''means check wether the stack is empty or the last item is not a closing sign, if so its false'''
#stack[-1]
'''refers to the last item currently in the stack list'''

print(isValid("([{}])"))
#"[(])"


# the for loop's big o is O(n), which makes the speed/efficiency also O(n)
# space complecxity is O(1)





