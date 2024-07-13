word = input()

letters = {}

for letter in word:
    if letter in letters.keys():
        letters[letter] += 1
    else:
        letters[letter] = 1

for key, value in letters.items():
    if int(value)>1:
        print(f"{key} {value}")