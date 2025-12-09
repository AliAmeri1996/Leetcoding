'''contain duplicate'''
def contain_duplicate(l):
    n = len(l)
    for i in range(n):
        for j in range(i+1, n):
            if l[i] == l[j]:
                return True
    return False  # only here, after the loops, careful where you put this
#do do it inside the loop, the loop should iterate through the whole list

'''Time: O(n²) (because of the nested loops).
Space: O(1) (doesn’t use extra memory, just comparisons).'''



def contain_duplicate(l):
    seen = set()
    for num in l:
        if num in seen:
            return True
        seen.add(num)
    return False


''' time: O(n)
space:O(n)'''