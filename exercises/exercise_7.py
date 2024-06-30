lst = input().split()

new_lst = []

for l in lst:
    if l not in new_lst:
        new_lst.append(l)

print(" ".join(sorted(new_lst, reverse = False)))