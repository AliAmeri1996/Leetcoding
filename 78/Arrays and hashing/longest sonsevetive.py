def longest_consecutive(nums):
    if not nums:
        return 0

    nums.sort()
    streak = 1
    longest = 1

    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1]:
            continue  # duplicate: ignore it (don’t count, don’t reset)
        elif nums[i] == nums[i - 1] + 1:
            streak += 1  # valid consecutive
        else:
            longest = max(longest, streak)
            streak = 1  # reset streak

    return max(longest, streak)


print(longest_consecutive([0,3,2,5,4,6,1,1]))

#elif nums[i] == nums[i - 1] + 1:
'''is true only when:

nums[i] is exactly one more than nums[i - 1]

In other words, the two numbers are consecutive (e.g., 3 follows 2, or 5 follows 4)'''

#longest = max(longest, streak)
'''longest = max(longest, streak)
This checks:

Which is bigger — the longest streak found so far, or the current streak we just finished

It updates longest to the bigger of the two'''