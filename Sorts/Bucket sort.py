def bucket_sort(arr):
    if len(arr) == 0:
        return arr

    # Step 1: Create buckets
    bucket_count = len(arr)
    max_value = max(arr)
    min_value = min(arr)
    bucket_range = (max_value - min_value) / bucket_count  # Range of each bucket

    # Initialise buckets
    buckets = [[] for _ in range(bucket_count)]

    # Step 2: Distribute elements into buckets
    for num in arr:
        bucket_index = int((num - min_value) / bucket_range)
        if bucket_index == bucket_count:  # Edge case for max value
            bucket_index -= 1
        buckets[bucket_index].append(num)

    # Step 3: Sort individual buckets
    for bucket in buckets:
        bucket.sort()

    # Step 4: Concatenate buckets into a single sorted list
    sorted_array = []
    for bucket in buckets:
        sorted_array.extend(bucket)

    return sorted_array