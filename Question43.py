def generate_even_tuple():
    original_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    even_numbers = [num for num in original_tuple if num % 2 == 0]
    even_tuple = tuple(even_numbers)
    print(even_tuple)

generate_even_tuple()
