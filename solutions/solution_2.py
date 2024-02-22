# Exercise 2 Solution: Squares Dictionary Generator

# Prompt the user for an integer 'n'
n = int(input("Enter an integer for 'n': "))

# Create a dictionary comprehension that generates keys from 1 to 'n' and their squares as values
squares_dict = {key: key**2 for key in range(1, n+1)}

# Print the generated dictionary
print(squares_dict)
