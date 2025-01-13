def find_numbers():
    print("Finding numbers divisible by 7 but not a multiple of 5 between 2000 and 3200...")
    result = [str(num) for num in range(2000, 3201) if num % 7 == 0 and num % 5 != 0]
    print("Here are the numbers:")
    print(", ".join(result))

find_numbers()
