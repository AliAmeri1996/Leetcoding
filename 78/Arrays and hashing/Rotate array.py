'''rotate Array depending on the k'''


def rotate(nums, k):
    n = len(nums)
    k = k % n  # Reduce k so it’s always within the range 0 to n-1. basically in the range of the length of nums"
    nums[:] = nums[-k:] + nums[:-k]
    return nums

# Example
nums = [1,2,3,4,5,6,7]
print(rotate(nums, 3))  # [5,6,7,1,2,3,4]


#nums[-k:]Takes the last k elements of the list.
#nums[:-k]Takes everything except the last k elements (from the start up to index -k).