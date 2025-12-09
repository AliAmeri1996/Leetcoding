def quick_sort(arr):
    if len(arr) <= 1:
        return arr  # Base case: already sorted if 1 or 0 elements

    pivot = arr[len(arr) // 2]  # Choose pivot (middle element)
    left = [x for x in arr if x < pivot]  # Elements smaller than pivot
    middle = [x for x in arr if x == pivot]  # Elements equal to pivot
    right = [x for x in arr if x > pivot]  # Elements greater than pivot

    return quick_sort(left) + middle + quick_sort(right)  # Recursively sort

# Example usage
arr = [64, 25, 12, 22, 11]
sorted_arr = quick_sort(arr)
print("Sorted array:", sorted_arr)
