def minSubArrayLen(target, nums):
    n = len(nums)
    left = 0
    total = 0
    min_len = float("inf")   # start with infinity (very large number)

    for right in range(n):
        total += nums[right]   # expand window to the right

        # shrink window from the left while total >= target
        while total >= target:
            min_len = min(min_len, right - left + 1)
            total -= nums[left]
            left += 1

    return 0 if min_len == float("inf") else min_len

print(minSubArrayLen(3,[-2, 1, -3, 4, -1, 2, 1, -5, 4]))