# Function to count how many negative numbers are in a list
def count_negative_numbers(numbers):
    # Count each number that is less than 0
    return sum(1 for i in numbers if i < 0)

# Example list
numbers = [10, -4, -6, 2, 5, 3, -15, -4]

# Display the number of negative values
print(count_negative_numbers(numbers))

#Output 4