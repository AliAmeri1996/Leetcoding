'''found the index and the number of common ratios'''

def countTriplets(arr, r):
    right = {}
    left = {}
    total = 0

    # Step 1: count frequencies in right
    for num in arr:
        right[num] = right.get(num, 0) + 1

    # Step 2: scan through arr
    for b in arr:
        # remove current b from right
        right[b] -= 1

        # count possible a and c
        if b % r == 0:
            a_count = left.get(b // r, 0)
            c_count = right.get(b * r, 0)
            total += a_count * c_count

        # add current b to left
        left[b] = left.get(b, 0) + 1

    return total



    



            




print(countTriplets([1,2,2,4],2))





# def countTriplets(arr, r):
#     n=len(arr)
#     total=0
#     seen=set()

#     for i in range(n):
#       for j in range(i + 1, n):
#           for k in range(j + 1, n):
#             if arr[j] == arr[i] * r and arr[k] == arr[j] * r:
#                     total+=1
#                     # order already respects the GP, no need to sort
                    
            
            
#     return total