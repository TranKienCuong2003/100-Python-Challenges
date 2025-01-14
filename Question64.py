def compute_sum(n):
    total = 0.0
    for i in range(1, n + 1):
        total += i / (i + 1)
    return total

n = int(input("Enter a positive integer (n > 0): "))

if n > 0:
    result = compute_sum(n)
    print(f"The result of the series is: {result:.2f}")
else:
    print("Please enter a value greater than 0.")
