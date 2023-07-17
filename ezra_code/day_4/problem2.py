def word_index(list):
    longest_word = ""
    for word in list:
        if len(word) > len(longest_word):
            longest_word = word
    if longest_word in list:
        return list.index(longest_word)
    else:
        return 0

words1 = ["Hate", "remorse", "vengeance"]

words2 = ["Love", "Hate"]
print(word_index(words2))