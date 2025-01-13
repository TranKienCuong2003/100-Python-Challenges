from collections import defaultdict

def word_frequency():
    sentence = input("Enter a sentence: ")
    
    words = sentence.split()
    
    frequency = defaultdict(int)
    
    for word in words:
        frequency[word] += 1
    
    for word in sorted(frequency.keys()):
        print(f"{word}:{frequency[word]}")

word_frequency()
