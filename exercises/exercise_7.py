lst = input().split()

new_lst = []

for l in lst:
    if l not in new_lst:
        new_lst.append(l)

new_lst = list(map(int, new_lst))
print(" ".join(list(map(str, sorted(new_lst, reverse = False)))))