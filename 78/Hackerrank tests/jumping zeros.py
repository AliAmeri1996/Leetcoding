def jumpingOnClouds(c):
    i = 0
    jumps = 0
    n = len(c)
    while i < n - 1:
        # Prefer a 2-step jump if it's in bounds and safe
        if i + 2 < n and c[i + 2] == 0:
            i += 2
        else:
            i += 1
        jumps += 1
        # this means both if and else
    return jumps


#i + 2 < n
'''"If I jump two clouds ahead, will I still be inside the list?"'''

#c[i + 2]
'''“look at the element that is two positions ahead of my current position i”.
'''


print(jumpingOnClouds([0,0,1,0,0,1,0]))

               

        

            





