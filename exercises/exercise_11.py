words = input().split()
before_words = {x:0 for x in range(len(words))}

for idx, word in enumerate(words):
    before_appearences = words[:idx].count(word)
    if before_appearences == 0:
        before_words[idx] = "NO"
    else:
        before_words[idx] = "YES"

print("\n".join(list(map(str, before_words.values()))))