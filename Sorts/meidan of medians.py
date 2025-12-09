def find_median(arr):
    """
    Helper function to find the median of a small list.
    """
    arr.sort()
    return arr[len(arr) // 2]

def median_of_medians(arr):
    """
    Finds a good pivot using the Median-of-Medians approach.
    """
    # Step 1: Divide the array into groups of 5
    if len(arr) <= 5:
        return find_median(arr)

    groups = [arr[i:i + 5] for i in range(0, len(arr), 5)]
    medians = [find_median(group) for group in groups]

    # Step 2: Recursively find the median of the medians
    return median_of_medians(medians)

def mom_select(arr, k):
    """
    Median-of-Medians algorithm to find the k-th smallest element (1-based index).
    """
    if len(arr) == 1:  # Base case: only one element
        return arr[0]

    # Step 1: Use Median-of-Medians to select a pivot
    pivot = median_of_medians(arr)

    # Step 2: Partition the array
    low = [x for x in arr if x < pivot]
    high = [x for x in arr if x > pivot]
    equal = [x for x in arr if x == pivot]

    # Step 3: Determine which part contains the k-th smallest element
    if k <= len(low):  # k-th smallest is in the lower part
        return mom_select(low, k)
    elif k > len(low) + len(equal):  # k-th smallest is in the upper part
        return mom_select(high, k - len(low) - len(equal))
    else:  # Pivot is the k-th smallest element
        return pivot

# Example usage
arr = [8, 1, 3, 7, 9, 2]
k = 5  # Find the 5th smallest element
print("5th smallest element (MoM):", mom_select(arr, k))
