string = input()

count = {"lower": 0,
          "upper": 0
}

for symbol in string:
    if symbol.islower():
        count["lower"] += 1
    elif symbol.isupper():
        count["upper"] += 1

print(f"UPPER {count['upper']} ")
print(f"LOWER {count['lower']} ")