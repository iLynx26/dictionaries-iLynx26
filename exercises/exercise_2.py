string = input()

count = {"letters": 0,
          "digits": 0
}

for symbol in string:
    if symbol.isdigit():
        count["digits"] += 1
    elif symbol.islower() or symbol.isupper():
        count["letters"] += 1

print(f"LETTERS {count['letters']} ")
print(f"DIGITS {count['digits']} ")