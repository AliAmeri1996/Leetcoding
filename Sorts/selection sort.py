def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]  # Swap
    return arr

# Example usage
arr = [64, 25, 12, 22, 11]
sorted_arr = selection_sort(arr)
print("Sorted array:", sorted_arr)


# for i = 1 to n - 1 do
#     elem = A[i]        // Assume the current element is the smallest
#     pos = i            // Store the position of the smallest element found
#     for j = i + 1 to n do
#         if A[j] < elem then
#             elem = A[j]   // Update the smallest element
#             pos = j       // Update the position of the smallest element
#         end if
#     end for
#     swap A[i] and A[pos]  // Place the smallest element at the correct position
# end for

#if arr[j] < arr[min_index]:
                #min_index = j
'''"If the element at index j is smaller than the currently
 known minimum element (at min_index), then update the minimum — because we just found a smaller one."'''

#Outer loop (i): Picks where to place the next smallest element.

#Inner loop (j): Scans the rest of the array to find that smallest element.
