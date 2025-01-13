def print_square_keys():
    square_dict = {}
    for i in range(1, 21):
        square_dict[i] = i ** 2
    
    for key in square_dict.keys():
        print(key)

print_square_keys()
