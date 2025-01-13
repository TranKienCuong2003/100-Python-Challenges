import math

def calculate_Q():
    C = 50
    H = 30
    D = input("Enter comma-separated values for D: ").split(",")
    result = []

    for d in D:
        Q = math.sqrt((2 * C * int(d)) / H)
        result.append(str(round(Q)))

    print(",".join(result))

calculate_Q()
