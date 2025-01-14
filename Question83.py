import timeit

code_to_measure = "1 + 1"

execution_time = timeit.timeit(code_to_measure, number=100)

print(f"Running time of '1 + 1' for 100 times: {execution_time} seconds")
