def merge(nums1, m, nums2, n):
    i = m - 1       # pointer for nums1
    j = n - 1       # pointer for nums2
    k = m + n - 1   # pointer for placement in nums1

    while j >= 0:
        if i >= 0 and nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
        k -= 1

#i = m - 1 
"""i is a pointer (index) to track the current element in nums1 (the valid part).
Since Python lists are 0-indexed, the last valid element in nums1 is at position m-1"""

#j = n - 1
"""j is a pointer to track the current element in nums2.
Starts at the end of nums2 (n - 1)."""

#k = m + n - 1
"""k is the pointer to track the position where we will place the next largest element in nums1.
Because nums1 has length m + n, the last index is m + n - 1."""

#Summary of pointers:
"""nums1: [1,2,3,0,0,0]
          i        k

   nums2: [2,5,6]
            j
"""

#while j >= 0:
"""Keep going until all elements from nums2 have been placed into nums1.
Once j < 0, nums2 is empty, and any remaining nums1 elements are already in place"""

#if i >= 0 and nums1[i] > nums2[j]:
"""Check two things:

Is there still a valid element left in nums1? (i >= 0)

Is nums1[i] larger than nums2[j]?

"""

