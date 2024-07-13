countries = {}

for i in range(int(input())):
    line = input().split()
    countries[line[0]] = line[1:]


for i in range(int(input())):
    city = input()
    for country in countries.keys():
        if city in countries[country]:
            print(country)

