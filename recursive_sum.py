def recursive_sum(lst):
    if len(lst)==1:
        return lst[0]
    return lst[0] + recursive_sum(lst[1:])

print(recursive_sum([2,3,4,5]))