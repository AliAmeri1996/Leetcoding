#A square of side length A is tiled by whole squares of side length B. Output the remaining area of the first square that is not covered by the tiled squares.

#If the second square is larger than the first square output ERROR.
#Input
#Line 1: An integer A for representing the side length of the first square
#Line 2: An integer B for representing the side length of the second square
#Output
#A single integer representing the remaining area of the first square not covered, or ERROR
#Constraints
#1 ≤ A ≤ 2^15
#0 ≤ B ≤ 2^15

def remaining_area():
    # Read inputs
    A = int(input("Enter side length of the first square (A): "))
    B = int(input("Enter side length of the second square (B): "))

    # Check if B is larger than A
    if B > A:
        print("ERROR")
        return

    # Compute the area of the first square
    area_A = A * A

    # Compute the area of a single smaller square
    area_B = B * B

    # Compute how many whole squares of side B fit into the first square
    if B > 0:
        num_squares_along_side = A // B
        total_squares = num_squares_along_side * num_squares_along_side
        covered_area = total_squares * area_B
    else:
        covered_area = 0

    # Calculate the remaining area
    remaining_area = area_A - covered_area

    # Output the remaining area
    print(remaining_area)

# Call the function
remaining_area()