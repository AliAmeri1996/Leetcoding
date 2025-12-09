def findMin(nums):
    smallest=nums[0]
    for i in range(1,len(nums)):
        if nums[i]<smallest:
            smallest==nums[i]
        return smallest
    


'''the big(o) is o(n)'''