alphabet = [chr(v) for v in range(97, 123)]
alphabet_numbered = []
sentence = input()

for letter in alphabet:
    alphabet_numbered.append(sentence.count(letter))

print(" ".join(list(map(str, alphabet_numbered))))