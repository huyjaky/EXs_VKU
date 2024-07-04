def string_analysis(s):
    words = s.split()
    print(words)
    num_words = len(words)
    print(f"Number of words: {num_words}")

    for i, word in enumerate(words):
        if word.isdigit():
            print(f"Number found: {word} at position {i}")


# Example usage:
s = "Today is Sunday and we don't need to wake up at 6 am"
string_analysis(s)
