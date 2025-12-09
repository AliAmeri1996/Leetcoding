'''Given two strings, determine if they share a common substring. A substring may be as small as one character.
'''

def twoStrings(s1, s2):
    char_map = {}

    # store all characters from s1
    for char in s1:#Take the string s1 and loop through it one character at a time, assigning each character to the variable char in turn.
        char_map[char] = 1  # value doesn't matter, we just mark its existence
        #if the character is repeated it still shows only once

    # check if any character in s2 is in the map
    for char in s2:
        if char in char_map:
            print("YES")
            return

    print("NO")



    