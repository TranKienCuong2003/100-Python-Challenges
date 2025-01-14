def count_characters(input_string):
    char_count = {}

    for char in input_string:
        char_count[char] = char_count.get(char, 0) + 1
    
    for char, count in char_count.items():
        print(f"{char},{count}")

input_string = input("Enter a string: ")

count_characters(input_string)
