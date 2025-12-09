'''Two strings are anagrams of each other if the 
letters of one string can be rearranged to form the other string. Given a string, 
find the number of pairs of substrings of the string that are anagrams of each other.'''


def sherlockAndAnagrams(s):
    counts = {}
    
    # Step 1: generate all substrings
    for start in range(len(s)):
        for end in range(start + 1, len(s) + 1):
            substring = s[start:end]
            
            # Step 2: make a sorted key to represent its anagram group
            key = ''.join(sorted(substring))
            #substring = "bca"-->['a', 'b', 'c'] with ' '.join-->key = "abc"
            
            # Step 3: count occurrences
            counts[key] = counts.get(key, 0) + 1
    
    # Step 4: count pairs
    total_pairs = 0
    for key, count in counts.items():
        if count > 1:#Only do this calculation if the key was seen more than once. number of substrings.If count > 1, there are at least two substrings in the group, meaning at least one anagram pair exists.
            total_pairs += (count * (count - 1)) // 2
            #how many distinct pairs of substrings you can make from a group of anagrams.
    
    return total_pairs




#for key, count in counts.items():
'''make each key and value a tuple,  counts = {"a": 2, "b": 3}
[("a", 2), ("b", 3)]
'''
        
    



