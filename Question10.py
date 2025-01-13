def remove_duplicates_and_sort():
    words = input("Enter a sequence of whitespace-separated words: ").split()
    unique_words = sorted(set(words))
    print(" ".join(unique_words))

remove_duplicates_and_sort()
