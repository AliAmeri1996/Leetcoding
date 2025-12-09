def factorial(x):
    fact = 1
    for i in range(1, x + 1):
        fact *= i
    return fact

x = int(input("Enter value for x: "))
n = int(input("Enter value for n: "))

# Permutations of x items taken n at a time
result = factorial(x) / factorial(x - n)
print(result)

