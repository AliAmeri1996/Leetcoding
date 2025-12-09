def merge_sort(arr):
    if len(arr) <= 1:
        return arr  # If the array has one or zero elements, it's already sorted

    mid = len(arr) // 2 #this gets the length of the list
    left=arr[:mid]#Means: take all elements from index 0 up to (but not including) mid
    right=arr[mid:]#Means: take all elements from index mid to the end of the array
    
    left_hand = merge_sort(left)  # Recursively sort the left half
    right_hand = merge_sort(right)  # Recursively sort the right half

    return merge(left_hand, right_hand)  # Merge the sorted halves


def merge(left, right):
    sorted_list = []
    i = j = 0  # Pointers for left and right halves

    # Merge elements from both halves in sorted order
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1

    # Add any remaining elements from left or right half
    sorted_list.extend(left[i:])
    sorted_list.extend(right[j:])

    return sorted_list


# Example usage:
arr = [38, 27, 43, 3, 9, 82, 10]
sorted_arr = merge_sort(arr)
print("Sorted array:", sorted_arr)
