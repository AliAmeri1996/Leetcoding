""" given an integer array, move all zeros to the end """

def moveZeros(nums):
    n = len(nums)
    i = 0  # Pointer to place the next non-zero element

    for j in range(n):
        if nums[j] != 0:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1

"""There is no return value.

Why?
Because this function modifies the list in place—it directly updates nums.

"""

nums = [0, 1, 0, 3, 12]
moveZeros(nums)
print(nums)

"""How it works:

i tracks the position where the next non-zero element should be placed.

j scans all elements.

If nums[j] is not zero, swap nums[j] with nums[i]:

This moves non-zero numbers forward.

Zeros naturally slide toward the end"""