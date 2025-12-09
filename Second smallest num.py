def second_smallest(n, numbers):
    """
    Returns the second smallest value among the list `numbers`,
    assuming it has length n (n >= 2).
    """
    # Edge case check:
    if n < 2:
        raise ValueError("Need at least two numbers to find the second smallest.")

    # Initialize smallest and second smallest to very large values:
    smallest = float('inf')
    second_smallest_val = float('inf')

    # Single pass through the numbers
    for x in numbers:
        if x < smallest:
            # Current x becomes the new smallest
            # Old smallest becomes the second smallest
            second_smallest_val = smallest
            smallest = x
        elif x < second_smallest_val:
            # If x is not smaller than the smallest but still
            # smaller than the second smallest, update second smallest
            second_smallest_val = x

    return second_smallest_val

n = 5
arr = [12, 2, 8, 3, 10]

print(second_smallest(n,arr))
