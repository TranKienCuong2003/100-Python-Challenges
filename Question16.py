def square_odd_numbers():
    numbers = input("Enter a sequence of comma-separated numbers: ").split(",")
    odd_numbers = [str(int(num)) for num in numbers if int(num) % 2 != 0]
    print(",".join(odd_numbers))

square_odd_numbers()
