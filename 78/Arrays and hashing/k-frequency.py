
'''Given an integer array nums and an integer k, 
return the k most frequent elements within the array.
'''

def frequent(nums, k):
    if not nums:
        return []

    seen = {}

    # count frequencies
    for i in nums:
        seen[i] = seen.get(i, 0) + 1

    # sort keys by frequency (descending)
    sorted_keys = sorted(seen, key=lambda x: seen[x], reverse=True)

    return sorted_keys[:k]




#freq.items()
'''returns this dictionary of freq which is like the following {1: 1, 2: 2, 3: 3, 4: 2}
as key-value pairs, it returns the dictiory as tuples like the following [(1, 1), (2, 2), (3, 3), (4, 2)] so each tuple is number 
and frequency of that number '''



#key=lambda x: x[1]
'''means: use the second element of each tuple (the frequency) as the sorting key.'''

#[-k:]
'''slice the last elements, what ever the k is, slice the last elements '''