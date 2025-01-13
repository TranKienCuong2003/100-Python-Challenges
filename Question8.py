def sort_words():
    words = input("Enter a comma-separated sequence of words: ").split(",")
    words.sort()
    print(",".join(words))

sort_words()
