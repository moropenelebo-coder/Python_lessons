# Function that counts letters and numbers in a sentence
def count_letters_numbers(sentence):

    # Counter for alphabetic characters (a-z, A-Z)
    letters = 0

    # Counter for numeric characters (0-9)
    numbers = 0

    # Loop through each character in the sentence
    for char in sentence:

        # Check if the character is a letter
        if char.isalpha():
            letters += 1

        # Check if the character is a digit
        elif char.isdigit():
            numbers += 1

    # Return both counts as a tuple (letters, numbers)
    return letters, numbers


# Example sentence
sentence = "Learning python in 2026"

# Call the function and unpack results
letters_count, number_count = count_letters_numbers(sentence)

# Print results
print("Letter", letters_count)
print("Numbers", number_count)

#Output Letter 16
#       Numbers 4