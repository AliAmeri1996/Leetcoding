'''Implement a function to search for target within nums'''

def search( nums, target):
    left=0
    right=len(nums) -1

    while left <=right:
        mid=(left+right)//2

        if nums[mid]==target:
            return mid
        elif nums[mid]<target:
            left=mid+1
        else:
            right=mid-1
    return -1
#“I looked everywhere, but the target isn’t in the list so return -1.”
    

        
print(search(nums = [-1,0,2,4,6,8], target = 4))


'''Move return -1 outside the loop so the function only returns -1 after checking all elements:'''

#while left <= right:
'''Keep searching as long as there’s still a valid range of elements to check.'''
