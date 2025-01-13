def generate_square_dict():
    n = int(input("Enter a number: "))
    square_dict = {i: i * i for i in range(1, n + 1)}
    print(square_dict)

generate_square_dict()
