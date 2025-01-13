from operator import itemgetter

def sort_tuples():
    data = input("Enter tuples (name, age, height) separated by commas: ").split(",")
    tuples = [tuple(item.split()) for item in data]
    
    sorted_tuples = sorted(tuples, key=itemgetter(0, 1, 2))
    
    print(sorted_tuples)

sort_tuples()
