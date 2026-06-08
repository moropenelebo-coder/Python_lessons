# Function to reverse the order of words in a sentence
def reverse_words_order(sentence):
    # Split the sentence into words, reverse the list,
    # and join the words back into a string
    return " ".join(sentence.split()[::-1])

# Example sentence
sentence = "hello world python"

# Display the sentence with the word order reversed
print(reverse_words_order(sentence))

#Output python world hello