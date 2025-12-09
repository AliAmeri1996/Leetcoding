''' Intersection of Two Arrays II'''

def intersection(nums1, nums2):
    nums1.sort()
    nums2.sort()
    i = j = 0
    res = []

    while i < len(nums1) and j < len(nums2):#Keep looping as long as both pointers (i and j) are still inside their respective lists.
        if nums1[i] == nums2[j]:
            res.append(nums1[i])# it means what it says
            i += 1# moving the pointer to the right
            j += 1# moving the pointer to the right
        elif nums1[i] < nums2[j]:
            i += 1
        else:
            j += 1
    return res
            


    
#If equal → record it. If not equal → discard the smaller one and move forward.

print(intersection([1,2,2,1],nums2 = [2,2]))