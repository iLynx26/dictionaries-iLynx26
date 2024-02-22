# Prompt the user for a list of integers
input_list = list(map(int, input("Enter a list of integers: ").split()))

# Remove duplicates by converting the list to a set, then convert back to a list and sort it
unique_list = sorted(set(input_list))

# Print the resulting list without duplicates
print(" ".join(map(str, unique_list)))
