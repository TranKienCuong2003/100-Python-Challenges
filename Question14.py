def count_case_letters():
    sentence = input("Enter a sentence: ")
    upper_case = 0
    lower_case = 0

    for char in sentence:
        if char.isupper():
            upper_case += 1
        elif char.islower():
            lower_case += 1

    print(f"UPPER CASE {upper_case}")
    print(f"LOWER CASE {lower_case}")

count_case_letters()
