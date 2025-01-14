import random

divisible_by_35 = range(35, 1001, 35)

random_numbers = random.sample(divisible_by_35, 5)

print(f"Random numbers divisible by 5 and 7 between 1 and 1000: {random_numbers}")
