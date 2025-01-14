input_list = [12, 24, 35, 24, 88, 120, 155, 88, 120, 155]

seen = set()

result = [x for x in input_list if not (x in seen or seen.add(x))]

print(result)
