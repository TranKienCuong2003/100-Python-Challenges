numbers = [12, 24, 35, 70, 88, 120, 155]

result = [num for index, num in enumerate(numbers) if index not in [0, 4, 5]]

print(result)
