number, unit_from, _,  unit_to = input().split()

conversion_to_meters = {
    "mile" : 1609,
    "yard" : 0.9144,
    "feet" : 0.3048,
    "inch" : 0.0254,
    "meter": 1,
    "kilometer" : 1000,
    "centimeter" : 0.01,
    "millimeter": 0.001
}

if unit_from == "miles":
   unit_from = "mile" 
elif unit_from == "feet":
   unit_from = "foot"
elif unit_from[-2:] == "es":
    unit_from = unit_from[:-2]
elif unit_from[-1:] == "s":
    unit_from = unit_from[:-1]

unit_to = unit_to[:-2] if unit_to[-2:] == "es" else unit_to[:-1]

print(f"{number = }")
print(f"{unit_from = }")
print(f"{unit_to = }")

meters = int(number) * conversion_to_meters[unit_from]
print(f"{meters = }")

result = meters / conversion_to_meters[unit_to]

print(result)