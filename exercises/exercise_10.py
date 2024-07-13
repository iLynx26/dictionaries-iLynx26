synonym_dict = {}

for i in range(int(input())):
    new_synonyms = input().split()
    if len(new_synonyms) > 2:
        synonym_dict[new_synonyms[0:1]] = new_synonyms[2]
    else:
        synonym_dict[new_synonyms[0]] = new_synonyms[1]

find_this_synonym = input()
if find_this_synonym in synonym_dict.keys():
    print(synonym_dict[find_this_synonym])
else:
    indx = list(synonym_dict.values()).index(find_this_synonym)
    print(list(synonym_dict.keys())[indx])