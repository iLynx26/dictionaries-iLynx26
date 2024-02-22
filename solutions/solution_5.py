# Exercise 5 Solution: Character Frequency in a String

# Prompt the user for a string
input_string = input("Enter a string: ")

# Initialize an empty dictionary to store character frequencies
char_frequency = {}

# Count each character's frequency
for char in input_string:
    char_frequency[char] = char_frequency.get(char, 0) + 1

# Iterate over the dictionary and print each character with its frequency
for char, frequency in char_frequency.items():
    print(f"{char} {frequency}")
