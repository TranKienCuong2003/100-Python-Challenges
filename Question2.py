def compute_factorial():
    num = int(input("Enter a number to compute its factorial: "))
    factorial = 1
    for i in range(1, num + 1):
        factorial *= i
    print(f"The factorial of {num} is: {factorial}")

compute_factorial()
