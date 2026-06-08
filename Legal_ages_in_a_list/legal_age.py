# Function to filter and return only legal ages (18 and above)
def legal_age(ages):
    # Create an empty list to store valid ages
    age_list = []

    # Loop through each age in the input list
    for age in ages:
        # Check if the age is 18 or older (legal age condition)
        if age >= 18:
            # Add valid age to the new list
            age_list.append(age)

    # Return the list of legal ages
    return age_list

# Example usage of the function
print(legal_age([1, 18, 21, 9, 5, 4, 45]))
# Expected output: [18, 21, 45]