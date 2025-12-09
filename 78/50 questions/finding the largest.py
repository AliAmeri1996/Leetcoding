'''finding the largest num in an unsorted array'''

def largest(l):
    if not l:  # handle empty list
        return None
    largest = l[0]
    for num in l:
        if num > largest:
            largest=num
    return largest

print(largest([7, 3, 9, 1, 4, 8, 2, 5, 6]))