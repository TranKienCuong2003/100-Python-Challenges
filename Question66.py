def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

n = int(input("Enter a positive integer (n >= 0): "))

if n >= 0:
    result = fibonacci(n)
    print(f"The Fibonacci number at position {n} is: {result}")
else:
    print("Please enter a non-negative integer.")
