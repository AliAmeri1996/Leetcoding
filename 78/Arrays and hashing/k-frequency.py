
'''Given an integer array nums and an integer k, 
return the k most frequent elements within the array.
'''

def top_k(numbers, k):
    freq = {}
    for num in numbers:
        if num not in freq:
            freq[num] = 0
        freq[num] += 1 # the product of the code till here {1: 1, 2: 2, 3: 3, 4: 2}

    result = sorted(freq.items(), key=lambda x: x[1])
    return [num for num, count in result[-k:]]



print(top_k([1,2,2,3,3,3,4,4],2))




#freq.items()
'''returns this dictionary of freq which is like the following {1: 1, 2: 2, 3: 3, 4: 2}
as key-value pairs, it returns the dictiory as tuples like the following [(1, 1), (2, 2), (3, 3), (4, 2)] so each tuple is number 
and frequency of that number '''



#key=lambda x: x[1]
'''means: use the second element of each tuple (the frequency) as the sorting key.'''

#[-k:]
'''slice the last elements, what ever the k is, slice the last elements '''