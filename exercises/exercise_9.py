words = input().split()
before_words = {x:0 for x in range(len(words))}

for idx, word in enumerate(words):
    before_appearences = words[:idx].count(word)
    before_words[idx] = before_appearences

print(" ".join(list(map(str, before_words.values()))))