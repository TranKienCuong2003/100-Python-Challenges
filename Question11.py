def check_divisibility_by_5():
    binary_numbers = input("Enter a sequence of comma-separated 4-digit binary numbers: ").split(",")
    divisible_by_5 = []

    for binary in binary_numbers:
        decimal = int(binary, 2)
        if decimal % 5 == 0:
            divisible_by_5.append(binary)

    print(",".join(divisible_by_5))

check_divisibility_by_5()
