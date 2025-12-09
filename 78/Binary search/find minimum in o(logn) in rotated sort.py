'''Find Minimum in Rotated Sorted Array
'''
#The only tricky part is they want you to find it in O(log n) time (binary search speed) instead of O(n) time (just scanning the list).


'''Given a rotated sorted array, find the smallest number.'''


def findMin(nums):
    left=0
    right =len(nums) - 1

   
    if nums[left] <= nums[right]:
        return nums[left]

    while left < right:
        mid = (left + right) // 2

        if nums[mid] > nums[right]: # so if the mid number is bigger than the last
            #number, then the smallest element is somewhere in the right half of the current range — possibly at mid itself — so we move the right pointer to mid.”
            left = mid + 1
        else:
            right = mid
            #“If the middle element is less than or equal to the rightmost element, then the smallest element must be somewhere on the left side of the array — and it could be at mid itself — so move right to mid.”

   
    return nums[left]


print(findMin([4,5,0,1,2,3]))


#if nums[left] <= nums[right]:
        #return nums[left]
'''If the first number is less than or equal to the last number,
it means the whole range is already sorted (no rotation break inside it).
the fist element is the smallest since its sorted list
'''