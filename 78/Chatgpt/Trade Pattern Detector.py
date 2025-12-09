'''Trade Pattern Detector'''
'''You are given a list of trade prices (integers) and must check if there’s an increasing subsequence of length 3 anywhere in the list.'''

def trade_pattern(nums):
    # Want to know if there exists i < j < k with nums[i] < nums[j] < nums[k]
    first = float('inf')   # smallest so far
    second = float('inf')  # second-smallest so far (after first)

    for x in nums:
        if x <= first:
            first = x                 # new smallest
        elif x <= second:
            second = x                # x is > first but <= second
        else:
            # we found x > second > first --> increasing triplet exists
            return True
    return False
