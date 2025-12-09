'''remove duplicate in a sorted array, two pointer'''

def remove_duplicates(arr):
    if not arr:
        return 0  # No elements

    # Pointer for the position of the next unique element
    j = 0  

    for i in range(1, len(arr)):
        if arr[i] != arr[j]:
            j += 1
            arr[j] = arr[i]#Hey, we found a new number — let’s save it in the unique section of the array."

    # unique_index + 1 is the length of the unique portion
    return arr[:j+1]

# Example
nums = [1, 1, 2, 2, 3, 3, 4]
print(remove_duplicates(nums))  # Output: [1, 2, 3, 4]




        
    

    