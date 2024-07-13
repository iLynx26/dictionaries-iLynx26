numbers = input().split()
duplicates = False

for number in numbers:
    if numbers.count(number) > 1:
        duplicates = True
output = ""
if duplicates:
    output = "duplicate list"
else:
    output = "is a unique sentence"
print(output)