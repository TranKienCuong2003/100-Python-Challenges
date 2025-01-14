import itertools

def print_permutations(input_list):
    permutations = itertools.permutations(input_list)
    
    for perm in permutations:
        print(perm)

input_list = [1, 2, 3]

print_permutations(input_list)
