def count_unique_pairs(nums, target):
    nums.sort() # O(n log n)
    i = 0
    j = len(nums) - 1
    seen_pairs = set() #Stores unordered, unique elements
    count = 0
     
    # O(n)
    while i < j:#This loop continues as long as the left pointer i is before the right pointer j also the 
        # loop should keep going to find more pairs
        current_sum = nums[i] + nums[j]
        if current_sum == target:
            if (nums[i], nums[j]) not in seen_pairs:
                seen_pairs.add((nums[i], nums[j]))
                count += 1
            i += 1
            j -= 1
        elif current_sum < target:
            i += 1
        else:
            j -= 1

    return count

# Test it
print(count_unique_pairs([1, 5, 7, -1, 5], 6))  # Output: 2

'''the big O of this code is O(n)'''