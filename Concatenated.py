try:  
    a, b = map(int, input("Enter two numbers: ").split())
    minus = a - b
    plus = a + b
    z = (str(minus) + str(plus))
    print(z)
except ValueError:
    print("Invalid input! Please enter exactly two integers.")

