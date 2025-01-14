def compute_f(n):
    if n == 0:
        return 1
    else:
        return compute_f(n - 1) + 100

n = int(input("Enter a positive integer (n > 0): "))

if n >= 0:
    result = compute_f(n)
    print(f"The result of f({n}) is: {result}")
else:
    print("Please enter a non-negative value for n.")
