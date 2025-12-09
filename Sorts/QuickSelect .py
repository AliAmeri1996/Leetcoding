import random
# k is the smallest number we want to find for example the 5th or the 6th
def quickselect(arr, k):
    """
    QuickSelect to find the k-th smallest element (1-based index) in the array.
    """
    if len(arr) == 1:  # Base case: only one element
        return arr[0]

    # Step 1: Choose a pivot (random choice)
    pivot = random.choice(arr)

    # Step 2: Partition the array
    low = [x for x in arr if x < pivot]
    high = [x for x in arr if x > pivot]
    equal = [x for x in arr if x == pivot]

    # Step 3: Determine which part contains the k-th smallest element
    if k <= len(low):  # k-th smallest is in the lower part
        return quickselect(low, k)
    elif k > len(low) + len(equal):  # k-th smallest is in the upper part
        return quickselect(high, k - len(low) - len(equal))
    else:  # Pivot is the k-th smallest element
        return pivot

# Example usage
arr = [8, 1, 3, 7, 9, 2]
k = 5  # Find the 5th smallest element
print("5th smallest element (QuickSelect):", quickselect(arr, k))
