'''Single Number'''

'''Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
You must implement a solution with a linear runtime complexity and use only constant extra space.'''

def single(nums):
    if not nums:
        return 0
    
    nums.sort()
    n = len(nums)
    
    # Check pairs
    for i in range(0, n - 1, 2):  # step by 2 because pairs should be side-by-side
        if nums[i] != nums[i + 1]:
            return nums[i]#will be the first element of a pair.
    
    # If not found in loop, the single is the last element
    return nums[-1]
            

print(single([2,2,1]))


# example of what does the iteration do 
#nums = [1, 1, 2, 2, 3, 3, 4] after its sorted 
#pairs=(1,1),(2,2),(3,3),4


# result = 0
# for num in nums:
#        result ^= num
# return result