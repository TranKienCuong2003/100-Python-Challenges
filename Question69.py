def divisible_by_5_and_7(n):
    for i in range(0, n + 1):
        if i % 5 == 0 and i % 7 == 0:
            yield i

n = int(input("Enter a positive integer (n >= 0): "))

if n >= 0:
    result = divisible_by_5_and_7(n)
    print(','.join(map(str, result)))
else:
    print("Please enter a non-negative integer.")
