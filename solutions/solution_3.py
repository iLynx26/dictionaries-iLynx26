# Exercise 3 Solution: Weekday Dictionary Lookup

# Define a dictionary mapping the names of the days of the week to their ordinal numbers
weekdays = {
    "Sunday": 0,
    "Monday": 1,
    "Tuesday": 2,
    "Wednesday": 3,
    "Thursday": 4,
    "Friday": 5,
    "Saturday": 6
}

# Prompt the user for the ordinal number of the day
day_number = int(input("Enter the ordinal number of the day: "))

# Find and print the day name by its ordinal number. If the input number is out of bounds, nothing is printed.
for day, number in weekdays.items():
    if number == day_number:
        print(day)
        break
