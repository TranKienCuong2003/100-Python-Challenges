def generate_list_and_tuple():
    numbers = input("Enter a sequence of comma-separated numbers: ")
    num_list = numbers.split(",")
    num_tuple = tuple(num_list)
    print(num_list)
    print(num_tuple)

generate_list_and_tuple()
