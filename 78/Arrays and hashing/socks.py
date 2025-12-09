'''There is a large pile of socks that must be paired by color. Given an array of integers representing the color of each sock, determine 
how many pairs of socks with matching colors there are.'''

def sockMerchant(n, ar):
    color_counts = {}
    for sock in ar:
        if sock in color_counts:
            color_counts[sock] += 1
            #Increase the count (value) for this sock color (key) by 1."
        else:
            color_counts[sock] = 1
            #Creates a new entry in the dictionary for this sock color and sets its count to 1.

    pairs = 0
    for count in color_counts.values():
        pairs += count // 2  # integer division to count how many pairs
        #this is how you count pairs

    return pairs

print(sockMerchant(7,[1,2,1,2,1,3,2]))