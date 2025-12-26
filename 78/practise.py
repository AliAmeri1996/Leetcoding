def bestbuyto(nums):
    if len(nums)==0:
        return 0
    smallest=nums[0]
    largest=nums[0]
    smallest_index = 0

    for i in  range (len(nums)):
        if nums[i]<smallest:
            smallest=nums[i]
            smallest_index=i

    largest = smallest

    for b in range (smallest_index, len(nums)):
        if nums[b]>largest:
            largest=nums[b]

    return largest-smallest

        
print(bestbuyto([7,1,5,3,6,4]))