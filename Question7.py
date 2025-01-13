def generate_2d_array():
    X, Y = map(int, input("Enter two digits X and Y (comma-separated): ").split(","))
    result = []

    for i in range(X):
        row = []
        for j in range(Y):
            row.append(i * j)
        result.append(row)

    print(result)

generate_2d_array()
