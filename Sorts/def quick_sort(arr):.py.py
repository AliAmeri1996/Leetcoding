def quick_sort(arr):

    if len(arr)<=1:
        return arr
    
    else:

        pivot=arr[-1]
        smaller,equal,larger=[],[],[]
        for num in arr:
            if num<pivot:
                smaller.append(num)
            elif num==arr:
                equal.append(num)
            else:
                larger.append(num)
            
            
    return quick_sort(smaller)+ equal + quick_sort
            

    