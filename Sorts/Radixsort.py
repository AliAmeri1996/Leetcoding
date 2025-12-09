def counting_sort(arr, exp):
    """Helper function to perform Counting Sort on a specific digit (exp)."""
    n = len(arr)
    output = [0] * n  # Output array to store sorted elements
    count = [0] * 10  # Count array for digits (0-9)

    # Count occurrences of each digit in the current place (exp)
    for num in arr:
        index = (num // exp) % 10
        count[index] += 1

    # Update count[i] to store the position of this digit in output[]
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Build the output array
    i = n - 1
    while i >= 0:
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1
        i -= 1

    # Copy the sorted elements back to the original array
    for i in range(n):
        arr[i] = output[i]

def radix_sort(arr):
    """Main function to perform Radix Sort."""
    # Find the maximum number to determine the number of digits
    max_num = max(arr)
    exp = 1  # Initialize the exponent (1 = least significant digit)

    # Perform Counting Sort for each digit (from least to most significant)
    while max_num // exp > 0:
        counting_sort(arr, exp)
        exp *= 10
