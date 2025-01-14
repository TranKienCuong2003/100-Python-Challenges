import re

s = input("Enter a string: ")

numbers = re.findall(r"\d+", s)

print(numbers)
