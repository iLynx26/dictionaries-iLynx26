lst = input().split()

dict_of_freq = {}

for word in lst:
    if word in dict_of_freq:
        dict_of_freq[word] += 1
    else:
        dict_of_freq[word] = 1

for key, value in dict_of_freq.items():
    print(f"('{key}', {value})", end="")