def fibonacci(n):
    fib_sequence = [0, 1] + [0]*(n-1)
    [fib_sequence.__setitem__(i, fib_sequence[i-1] + fib_sequence[i-2]) for i in range(2, n+1)]
    return fib_sequence

n = int(input("Enter a positive integer (n >= 0): "))

if n >= 0:
    result = fibonacci(n)
    print(','.join(map(str, result)))
else:
    print("Please enter a non-negative integer.")
