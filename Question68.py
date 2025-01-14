def even_numbers(n):
    for i in range(0, n + 1, 2):
        yield i

n = int(input("Enter a positive integer (n >= 0): "))

if n >= 0:
    result = even_numbers(n)
    print(','.join(map(str, result)))
else:
    print("Please enter a non-negative integer.")
