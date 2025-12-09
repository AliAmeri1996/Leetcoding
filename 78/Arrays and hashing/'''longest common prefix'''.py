'''longest common prefix'''

def longest_common_prefix(words):
    if not words:
        return ""

    prefix = ""
    # zip(*words) groups characters column by column
    for chars in zip(*words):#(*words) The * operator in Python is the unpacking operator,It doesn’t care if the elements are in a list, tuple, or set
        if len(set(chars)) == 1:     # all characters in this column are equal
            prefix += chars[0]# this is basically the first element of ('l','l','l').
        else:
            break
    return prefix



words = ["flower","flow","flight"]
print(longest_common_prefix(words))


#zip()
'''('f','f','f')   # first letters
('l','l','l')   # second letters
('o','o','i')   # third letters
('w','w','g')   # fourth letters
'''

'''But zip stops after 4 steps (the length of "flow", the shortest word).'''
