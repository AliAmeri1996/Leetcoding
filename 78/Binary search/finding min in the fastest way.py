def min_in_sorted(nums):
    if not nums:
        raise ValueError("empty list")
    # Ascending (or all equal)
    if nums[0] <= nums[-1]:
        return nums[0]
    # Strictly descending
    return nums[-1]

#if nums[0] <= nums[-1]'' this is the last element of the list'':
        #return nums[0]
'''is a quick check for whether the list is already sorted in ascending order (or all elements are equal).'''
