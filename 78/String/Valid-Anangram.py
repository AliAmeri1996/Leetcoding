'''anangram is when all the characters of two words are the same, regrdless of how 
they're sorted'''


def anagram(a, b):
    if len(a) != len(b):
        return False
    
    count = {}
    
    
    for char in a:  #O(n)
        count[char] = count.get(char, 0) + 1 # count = {'l': 1, 'i': 1, 'a': 1}
    
    
    for char in b:      #O(n)
        if char not in count:
            return False
        count[char] -= 1 # subtract from the value of the key
        if count[char] < 0:
            return False
    
    # If all counts are zero, it's an anagram
    return True

print(anagram("lia", "ali"))     # True
print(anagram("stone", "tones")) # True
print(anagram("stone", "note"))  # False

# big O = O(n)
# space complixity=O(1)


    

        