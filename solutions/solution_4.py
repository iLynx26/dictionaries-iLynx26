# Exercise 4 Solution: Character Count Dictionary from String

# Prompt the user for a string
input_string = input("Enter a string: ")

# Initialize an empty dictionary to store character counts
char_count_dict = {}

# Iterate over each character in the string
for char in input_string:
    # If the character is already in the dictionary, increment its count
    if char in char_count_dict:
        char_count_dict[char] += 1
    # Otherwise, add the character to the dictionary with a count of 1
    else:
        char_count_dict[char] = 1

# Print the character count dictionary
print(char_count_dict)
