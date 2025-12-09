def twoSum(nums, target):
    seen = {}   # value -> index
    for i, num in enumerate(nums):# i is index and num is the value
        complement = target - num
        if complement in seen:        # if we've already seen the partner
            return [seen[complement], i] # seen[complement] this gives the value
        seen[num] = i  
        #First loop (i=0, num=3):
        #seen[3] = 0 → now seen = {3: 0}  

#o(n)

print(twoSum([3, 2, 4],6))


#complement = target - num
'''num = 3
complement = 6 - 3 = 3 → we’d need another 3 to reach 6.'''


#return [seen[complement], i] 
'''seen[complement] gives the index where the partner number was stored earlier.
i is the index of the current number.'''





#Time: O(n²)

# def twoSum(nums, target):
#     n = len(nums)
#     for i in range(n):
#         for j in range(i+1, n):
#             if nums[i] + nums[j] == target:
#                 return [i, j]
