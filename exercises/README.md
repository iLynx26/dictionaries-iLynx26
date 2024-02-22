# Exercises 🏋️‍♂️

## Topics Covered:
- Dictionaries

---

## Exercise 1: Search Engine Market Share Tracker

**Objective:** Create a program that holds information about the market share of various search engines in a dictionary.

### Specifications:
- **Data Structure:**
  - Use a dictionary where:
    - Keys are the names of the search engines (str).
    - Values are their respective market shares in the world at the moment (float).

- **Output:**
  - Print the elements of the dictionary as shown in the expected outputs.

### Example Usage:

| No. | Inputs | Expected Outputs |
|---|--------|------------------|
|1 | None   | Yahoo!: 2.09     |
||        | Google: 90.15    |
||        | Bing: 3.23       |
||        | Baidu: 2.2       |

---

## Exercise 2: Squares Dictionary Generator

**Objective:** Write a program that generates and prints a dictionary where keys are integers from 1 to `n` (inclusive) and values are the squares of the keys. `n` is an integer input provided by the user.

### Specifications:
- **Input:**
  - `n` (int): The upper limit of the range, provided by the user.

- **Output:**
  - A dictionary where:
    - Keys are integers from 1 to `n`.
    - Values are the squares of the keys.

### Example Usage:

| No. | Inputs | Expected Outputs |
|-----|--------|------------------|
| 1   | 15     | {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225} |
| 2   | 5      | {1: 1, 2: 4, 3: 9, 4: 16, 5: 25} |

---

## Exercise 3: Weekday Dictionary Lookup

**Objective:** Create a program that constructs a dictionary where keys are the names of the days of the week, and values are integers representing the day's ordinal number from 0 to 6. Print the name of the day for a given ordinal number input. If the input ordinal number is out of bounds, the program should not print or report any errors.

### Specifications:
- **Data Structure:**
  - A dictionary with:
    - Keys as the names of the days of the week (str).
    - Values as the ordinal numbers of the days from 0 to 6 (int).

- **Input:**
  - An integer representing the ordinal number of the day.

- **Output:**
  - The name of the day corresponding to the input ordinal number.

### Example Usage:

| Inputs | Expected Outputs |
|--------|------------------|
| 3      | Wednesday        |
| 0      | Sunday           |

This exercise involves handling user input to retrieve information from a predefined dictionary without error messages for invalid inputs.


---
