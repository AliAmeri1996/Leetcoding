
'''This is the famous "Maximum Subarray" problem from Leetcode (#53).
You’re given an array of integers (can be positive or negative), and your goal is to find the contiguous subarray with the maximum sum.

🧩 Problem:
python
Copy code
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
The subarray [4, -1, 2, 1] has the largest sum = 6'''




def maxSubArray(nums):
    maxSum=nums[0] #We initialize maxSum = nums[0] to ensure the algorithm works even when all numbers are negative, because the maximum subarray must contain at least one element.
    current_sum=0

    for n in nums:
        if current_sum< 0: #If the running sum so far (current_sum) has become negative, then keeping it will only hurt any future subarray you try to build.
            current_sum=0  # therefor we reset and start fresh from the next element.
        current_sum+=n
        maxSum=max(maxSum,current_sum) #“Is my current subarray better than the best I’ve ever seen?”

    return maxSum
    
print(maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))



#current_sum = max(nums[i], current_sum + nums[i])
'''At position i, the best subarray ending exactly at this index is either:

just the element itself (nums[i]), or

the element added to the best subarray that ended at the previous index (current_sum + nums[i]).”'''
