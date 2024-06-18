# Exercises 🏋️‍♂️

## Topics Covered:
- Dictionaries

<!-- 513 -->

## Exercise 1: Day of the Week Dictionary - Easy 😊 (Est. Time: 5-10 mins | Points: 10)

**Problem:** Create a dictionary where the keys are the names of the days of the week, and the values are integers representing the ordinal number of the day of the week from 0 to 6. Print the name of the day for the entered ordinal number. If the entered number is out of bounds, the program does not print any message or indicate an error.

### Input:
- An integer representing the ordinal number of the day.

### Output:
- The name of the day corresponding to the ordinal number, or no output if the number is out of bounds.

### Examples:

| No. | Inputs | Outputs   |
| --- | ------ | --------- |
| 1   | 3      | Wednesday |
| 2   | 0      | Sunday    |
| 3   | 5      | Friday    |
| 4   | 7      |           |

### Note:
This exercise tests the ability to use dictionaries for key-value mappings in Python.


<!-- 519 -->

## Exercise 2: Count Letters and Digits - Easy 😊 (Est. Time: 10 mins | Points: 10)

**Problem:** Write a program that takes a string of characters and calculates the number of letters and digits.

### Input:
- A string of characters.

### Output:
- The count of letters and digits in the format:
```
LETTERS {count}
DIGITS {count}
```

### Examples:

| No. | Inputs                                    | Outputs               |
| --- | ----------------------------------------- | --------------------- |
| 1   | Project Gutenberg offers over 59,000 free eBooks | LETTERS 36<br>DIGITS 5   |
| 2   | 123abc456def                              | LETTERS 6<br>DIGITS 6    |
| 3   | 9876543210                                | LETTERS 0<br>DIGITS 10   |
| 4   | abcdefghijklmnopqrstuvwxyz                | LETTERS 26<br>DIGITS 0   |

### Note:
This exercise tests the ability to work with strings and count specific character types in Python.

<!-- 520 -->

## Exercise 3: Count Upper and Lower Case Letters - Easy 😊 (Est. Time: 10 mins | Points: 10)

**Problem:** Write a program that takes a string of characters and calculates the number of uppercase and lowercase letters.

### Input:
- A string of characters.

### Output:
- The count of uppercase and lowercase letters in the format 
```
UPPER CASE {count}
LOWER CASE {count}
```

### Examples:

| No. | Inputs                                    | Outputs               |
| --- | ----------------------------------------- | --------------------- |
| 1   | The quick brown FOX jumps over a lazy DOG | UPPER CASE 7<br>LOWER CASE 26 |
| 2   | Hello World                               | UPPER CASE 2<br>LOWER CASE 8  |
| 3   | PYTHON programming                        | UPPER CASE 6<br>LOWER CASE 11 |
| 4   | ABCdefGHIjklMNO                           | UPPER CASE 9<br>LOWER CASE 6  |

### Note:
This exercise tests the ability to work with strings and count specific character cases in Python.

<!-- 522 -->

## Exercise 4: Character Frequency Count - Easy 😊 (Est. Time: 10 mins | Points: 10)

**Problem:** Write a program to count the frequency of each character in the given string.

### Input:
- A string of characters.

### Output:
- The frequency of each character in the format "character count", each on a new line.

### Examples:

| No. | Inputs | Outputs  |
| --- | ------ | -------- |
| 1   | google | g 2<br>o 2<br>l 1<br>e 1 |
| 2   | hello  | h 1<br>e 1<br>l 2<br>o 1 |
| 3   | python | p 1<br>y 1<br>t 1<br>h 1<br>o 1<br>n 1 |
| 4   | abcabc | a 2<br>b 2<br>c 2 |

### Note:
This exercise tests the ability to count the frequency of characters in a string in Python.

<!-- 527 -->

## Exercise 5: Morse Code Representation - Easy 😊 (Est. Time: 10 mins | Points: 10)

**Problem:** Use a dictionary to output the Morse code representation of the letter entered by the user. The program should handle both uppercase and lowercase letters.

### Input:
- A letter entered by the user.

### Output:
- The Morse code representation of the letter.

### Examples:

| No. | Inputs | Outputs  |
| --- | ------ | -------- |
| 1   | D      | -..      |
| 2   | f      | ..-.     |
| 3   | A      | .-       |
| 4   | z      | --..     |

### Note:
This exercise tests the ability to use dictionaries and handle character case in Python.


<!-- 531 -->

## Exercise 6: Date Range Check - Easy 😊 (Est. Time: 10 mins | Points: 10)

**Problem:** Given a month and year for two dates (e.g., 12.2014 and 6.2019), the user enters another date (month and year). Determine if the third date falls within the range from the first date to the second date inclusive. The program should output `YES` or `NO`.

### Input:
- A year and month for the third date.

### Output:
- `YES` if the third date falls within the range, `NO` otherwise.

### Examples:

| No. | Inputs  | Outputs |
| --- | ------- | ------- |
| 1   | 2018<br>5 | YES   |
| 2   | 2014<br>11 | NO  |
| 3   | 2019<br>7 | NO   |
| 4   | 2016<br>3 | YES  |

### Note:
This exercise tests the ability to compare dates in Python.


