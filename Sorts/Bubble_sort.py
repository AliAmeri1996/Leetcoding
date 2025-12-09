def bubble_sort_optimized(arr):
    times=0
    n= len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - 1):#for j in range(0, n - i - 1) is the optimization version
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
                times+=1
        if not swapped:
            break  # Already sorted
    return arr,times



print(bubble_sort_optimized([2,6,3,2,4,5]))

#for j in range(0, n - 1):
'''n  - 1 is an optimization to avoid redundant comparisons'''

# the comparisons should be between two numbers, therefore the comparison should stop
#before the last elemnet since after that there wouldnt be two elemnts, the last one is only one left


'''Why n - 1 in range(0, n - 1)?
Because you're comparing pairs of elements:
arr[j] and arr[j + 1]

So you need to stop one element before the end of the list — otherwise arr[j + 1] will go out of bounds.'''