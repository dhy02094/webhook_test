def word_count(text):
    words = text.split(" ")
    word_freq = {}
    for word in words:
        word = word.lower().strip(",.!?")
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1
    return word_freq

def most_frequent_word(word_freq):
    max_word = None
    max_count = 0
    for word, count in word_freq.items():
        if count > max_count:
            max_word = word
            max_count = count
    return max_word, max_count

text = "Hello, hello! How are you? I hope you are doing well. Well, well..."
word_freq = word_count(text)
most_common_word, count = most_frequent_word(word_freq)

print(f"The most common word is '{most_common_word}' with a count of {count}.")
