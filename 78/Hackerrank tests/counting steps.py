def countingValleys(steps, path):
    altitude = 0
    valleys = 0

    for step in path:
        if step == 'U':
            altitude += 1
            if altitude == 0:
                valleys += 1  
        else:
            altitude -= 1

    return valleys

# Sample Input
print(countingValleys(8, 'UDDDUDUU'))  # Output: 1
