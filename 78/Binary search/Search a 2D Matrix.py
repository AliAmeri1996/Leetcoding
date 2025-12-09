'''Search a 2D Matrix with binary search method in o(log n)'''
def searchMatrix( matrix, target):
    if not matrix or not matrix[0]:
        return False
    
    rows=len(matrix)
    column=len(matrix[0])

    left=0
    right=rows*column -1

    while left<=right:
        mid=(left+right)//2
        mid_value=matrix[mid//column][mid%column]

        if mid_value==target:
            return True
        elif mid_value<target:
            left= mid +1
        else:
            right =mid -1

    return False
    
    

print(searchMatrix(matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]], target = 10))

#not matrix
'''(no rows at all).
'''
#not matrix[0]
'''(no columns).'''

#matrix[mid // column]
''' which row the element is in.'''

#mid % cols
'''Which column inside that row.'''

#mid_value = matrix[mid // column][mid % column]
'''Take the mid index from our pretend 1D list, and figure out which row and column it maps to in the real 2D matrix.'''
'''mid_value = matrix[1][2]  '''