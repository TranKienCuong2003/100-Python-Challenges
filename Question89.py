numbers = [12, 24, 35, 70, 88, 120, 155]

filtered_numbers = [num for index, num in enumerate(numbers) if index % 2 != 0]

print(filtered_numbers)
