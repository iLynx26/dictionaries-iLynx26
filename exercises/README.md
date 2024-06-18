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

<!-- 535 -->

## Exercise 7: Remove Duplicates from List - Medium 🔥 (Est. Time: 10-15 mins | Points: 20)

**Problem:** Write a program to remove duplicates from a list of integers.

### Input:
- A list of integers entered in a single line.

### Output:
- The list of integers with duplicates removed, sorted in ascending order.

### Examples:

| No. | Inputs                | Outputs               |
| --- | --------------------- | --------------------- |
| 1   | 10 5 11 2 3 5 8 9 3 4 2 | 2 3 4 5 8 9 10 11     |
| 2   | 1 1 1 1 1 1             | 1                     |
| 3   | 5 4 3 2 1               | 1 2 3 4 5             |
| 4   | 2 2 3 3 4 4 5 5         | 2 3 4 5               |

### Note:
This exercise tests the ability to work with lists and remove duplicate elements in Python.

<!-- 544 -->

## Exercise 8: Count Character Occurrences - Medium 🔥 (Est. Time: 10-15 mins | Points: 20)

**Problem:** Write a program that counts and prints the number of occurrences of each character in the input string.

### Input:
- A string of characters.

### Output:
- The count of each character in the string, printed in the order of their first appearance.

### Examples:

| No. | Inputs        | Outputs            |
| --- | ------------- | ------------------ |
| 1   | abcabcdfghj   | a, 2<br>b, 2<br>c, 2<br>d, 1<br>f, 1<br>g, 1<br>h, 1<br>j, 1 |
| 2   | hello world   | h, 1<br>e, 1<br>l, 3<br>o, 2<br> , 1<br>w, 1<br>r, 1<br>d, 1 |
| 3   | aabbcc        | a, 2<br>b, 2<br>c, 2 |
| 4   | programming   | p, 1<br>r, 2<br>o, 1<br>g, 2<br>m, 2<br>a, 1<br>i, 1<br>n, 1 |

### Note:
This exercise tests the ability to count and print character occurrences in Python.


<!-- 549 -->

## Exercise 9: Count Previous Occurrences of Words - Medium 🔥 (Est. Time: 10-15 mins | Points: 20)

**Problem:** Given a line of text, a word is defined as a sequence of non-space characters that are contiguous. Words are separated by one or more spaces or end-of-line characters. For each word in this text, count how many times it has appeared before in this text.

### Input:
- A line of text.

### Output:
- For each word in the text, print how many times it has appeared before.

### Examples:

| No. | Inputs                                   | Outputs               |
| --- | ---------------------------------------- | --------------------- |
| 1   | var list set tuple list tuple tuple dict var | 0 0 0 0 1 1 2 0 1     |
| 2   | hello world hello hello world             | 0 0 1 2 1             |
| 3   | a b c a b c a b c                         | 0 0 0 1 1 1 2 2 2     |
| 4   | one two one two three two four three      | 0 0 1 1 0 2 0 1       |

### Note:
This exercise tests the ability to count the number of previous occurrences of words in a text in Python.


<!-- 556 -->

## Exercise 10: Find Synonym - Medium 🔥 (Est. Time: 10-15 mins | Points: 20)

**Problem:** Given a dictionary consisting of pairs of words. Each word is a synonym for the paired word. All words in the dictionary are different. For a given word, determine its synonym. The program receives the number of synonym pairs `n`. Then `n` lines follow, each line containing exactly two synonymous words. After that, one word is entered. The program should print the synonym for the given word.

### Input:
- An integer `n` representing the number of synonym pairs.
- `n` lines, each containing exactly two synonymous words.
- One word for which the synonym needs to be determined.

### Output:
- The synonym for the given word.

### Examples:

| No. | Inputs                     | Outputs  |
| --- | -------------------------- | -------- |
| 1   | 3<br>Solar Heliac<br>Day Daytime<br>Arrive Occur<br>Heliac | Solar    |
| 2   | 2<br>Happy Joyful<br>Sad Unhappy<br>Joyful | Happy    |
| 3   | 4<br>Big Large<br>Small Tiny<br>Fast Quick<br>Smart Intelligent<br>Quick | Fast |
| 4   | 1<br>Hot Warm<br>Warm | Hot |

### Note:
This exercise tests the ability to work with dictionaries and find corresponding pairs in Python.

