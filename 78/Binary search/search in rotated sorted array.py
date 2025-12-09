'''You’re given an array of integers nums that was originally sorted in ascending order, but then rotated at some pivot index.
Example: [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2].
You’re also given a target value. Your job is to find the index of the target in nums using O(log n) time. If it’s not there, return -1.'''


def search(nums, target):
    left=0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        # Found the target
        if nums[mid] == target:
            return mid

        # Check if left half is sorted
        if nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1  # target is in the left half
            else:
                left = mid + 1   # target is in the right half
        # Otherwise, right half must be sorted
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1   # target is in the right half
            else:
                right = mid - 1  # target is in the left half

    return -1


print(search([4,5,6,7,0,1,2], 0))