def group_anagrams(words):
    anagrams = {}
    for word in words:
        # Create the sorted key
        key = ''.join(sorted(word))

        
        # If the key is not in the dictionary, create a new list
        if key not in anagrams:
            anagrams[key] = []
        # Append the word to the corresponding group
        anagrams[key].append(word)
    # Return the groups as a list of lists
    return list(anagrams.values())

print(group_anagrams(["act","pots","tops","cat","stop","hat"]))
          

    
#key = ''.join(sorted(word))          
#This makes a key that is the same for all anagrams.

#Example:
#"cat" → "act"
#"act" → "act"
#"tac" → "act"
#O(n · k log k) ,sorted(word), Takes O(k log k)


#anagrams[key] = []
'''this means that in the right side of the hash create an empty list'''
#anagrams[key].append(word)
'''this basically means add to the list in the right side of the hash/values'''
    
               
               
            
 




