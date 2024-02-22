# Prompt the user for a list of integers
input_list = list(map(int, input("Enter a list of integers: ").split()))

# Initialize an empty dictionary to count occurrences of each value
value_counts = {}

# Populate the dictionary with values from the list
for value in input_list:
    # If the value is already in the dictionary, increment its count
    if value in value_counts:
        value_counts[value] += 1
    # Otherwise, add the value to the dictionary with a count of 1
    else:
        value_counts[value] = 1

# The number of unique values is the number of keys in the dictionary
unique_count = len(value_counts.keys())

# Print the number of unique values
print(unique_count)
