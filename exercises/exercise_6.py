year = int(input())
month = int(input())

if 2014 < year < 2019:
    print("YES")
elif year > 2019 or year < 2014:
    print("NO")
elif year == 2019:
    if month <= 6:
        print("YES")
    else:
        print("NO")
elif year == 2014:
    if month == 12:
        print("YES")
    else:
        print("NO")