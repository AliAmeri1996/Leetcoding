def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):# start from the second element
        key = arr[i]# pointer number 1
        j = i - 1 #pointer number 2, the left side of the element

        while j >= 0 and arr[j] > key:#While elements to the left of key are greater, shift them right
            #the j pointer starts from zero all the way to the last element
            # j>=0 means you dont go out of the bound
            arr[j + 1] = arr[j]#This line shifts the element at index j one position to the right, into index j + 1.
            j -= 1# this keeps moving j to the left after first, second and third comparison 
            #moving left to compare more
        arr[j + 1] = key  # Insert the key in its correct position
    return arr

# Example usage
arr = [64, 25, 12, 22, 11]
sorted_arr = insertion_sort(arr)
print("Sorted array:", sorted_arr)

#this is a shifting sort

