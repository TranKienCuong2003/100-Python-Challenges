def print_square_values():
    square_dict = {}
    for i in range(1, 21):
        square_dict[i] = i ** 2
    
    for value in square_dict.values():
        print(value)

print_square_values()
