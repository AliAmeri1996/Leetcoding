numbers = input("Enter numbers without spaces: ").split()  # Example: "1234"

# Convert each character into an integer
numbers = list(map(int, numbers))  #Converts a sequence of characters (digits in a string) into a list of integers.
#"1234" to [1,2,3,4]
# Double each number
doubled = list(map(lambda x: x * 2, numbers))

print(doubled)  # Output: [2, 4, 6, 8] for input "1234"

