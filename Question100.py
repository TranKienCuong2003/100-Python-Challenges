def solve_puzzle():

    for chickens in range(36):
        rabbits = 35 - chickens
        if 2 * chickens + 4 * rabbits == 94:
            return chickens, rabbits

chickens, rabbits = solve_puzzle()
print(f"There are {chickens} chickens and {rabbits} rabbits.")
