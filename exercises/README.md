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
|1 | None   | Yahoo!: 2.09<br>Google: 90.15<br>Bing: 3.23<br>Baidu: 2.2       |

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

| No. | Inputs | Expected Outputs |
|-----|--------|------------------|
| 1   | 3      | Wednesday        |
| 2   | 0      | Sunday           |

This exercise involves handling user input to retrieve information from a predefined dictionary without error messages for invalid inputs.


---

## Exercise 4: Character Count Dictionary from String

**Objective:** Write a program that creates a dictionary from an input string to count the occurrence of each character.

### Specifications:
- **Input:**
  - A string from which to count characters.

- **Output:**
  - A dictionary where:
    - Keys are characters from the input string.
    - Values are the counts of each character's occurrences in the string.

### Example Usage:

| No. | Inputs                        | Expected Outputs                                                                                                                                 |
|-----|-------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------|
| 1   | Lorem ipsum dolor sit amet    | {'L': 1, 'o': 3, 'r': 2, 'e': 2, 'm': 3, ' ': 4, 'i': 2, 'p': 1, 's': 2, 'u': 1, 'd': 1, 'l': 1, 't': 2, 'a': 1}                                  |
| 2   | hello world                  | {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}                                                                                  |
| 3   | character                    | {'c': 2, 'h': 2, 'a': 2, 'r': 2, 'e': 1, 't': 1}                                                                                                   |

This exercise focuses on iterating over the characters in a string, counting their occurrences, and storing these counts in a dictionary for output.


---

## Exercise 5: Character Frequency in a String

**Objective:** Write a program to count the frequency of characters in a given string.

### Specifications:
- **Input:**
  - A string of characters provided by the user.

- **Output:**
  - The frequency of each character in the string, printed as separate lines for each character.

### Example Usage:

| No. | Inputs    | Expected Outputs |
|-----|-----------|------------------|
| 1   | google    | g 2              |
|     |           | o 2              |
|     |           | l 1              |
|     |           | e 1              |
| 2   | test      | t 2              |
|     |           | e 1              |
|     |           | s 1              |
| 3   | character | c 2              |
|     |           | h 2              |
|     |           | a 2              |
|     |           | r 2              |
|     |           | t 1              |
|     |           | e 1              |

The exercises showcase two approaches to counting character frequencies: one using a dictionary for a cumulative count and the other printing frequencies directly from the string.


---

## Exercise 6: Remove Duplicates from List

**Objective:** Write a program to remove duplicates from a list of integers.

### Specifications:
- **Input:**
  - A list of integers, where duplicates may exist.

- **Output:**
  - A list of integers with duplicates removed and elements sorted in ascending order.

### Example Usage:

| No. | Inputs                              | Expected Outputs         |
|-----|-------------------------------------|--------------------------|
| 1   | 10 5 11 2 3 5 8 9 3 4 2             | 2 3 4 5 8 9 10 11        |
| 2   | 1 2 3 4 5 1 2 3                     | 1 2 3 4 5                |
| 3   | 7 8 9 7 8 9                         | 7 8 9                    |

---
