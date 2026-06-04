
# Function that counts how many times each character
# appears in a word and returns the result as a dictionary
def frequency(word):

    # Create an empty dictionary to store character counts
    result = {}

    # Loop through each character in the word
    for char in word:

        # If the character already exists in the dictionary,
        # increase its count by 1
        if char in result:
            result[char] += 1

        # Otherwise, add the character to the dictionary
        # with an initial count of 1
        else:
            result[char] = 1

    # Return the dictionary containing character frequencies
    return result


# Example word
word = "sentence"

# Print the frequency of each character
print(frequency(word))