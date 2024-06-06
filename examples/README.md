# Examples 🏋️‍♂️

<!-- 512 -->
## Example 1: Print Dictionary Elements - Easy 😊 (Est. Time: 10 mins | Points: 10)

**Problem:** Print the elements of a dictionary where keys are numbers from `1` to `n` (both inclusive) and values are the squares of the keys. `n` is an integer input provided by the user.

| No. | Inputs | Outputs |
| --- | ------ | ------- |
| 1   | 5      | {1: 1, 2: 4, 3: 9, 4: 16, 5: 25} |
| 2   | 3      | {1: 1, 2: 4, 3: 9} |
| 3   | 7      | {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49} |
| 4   | 1      | {1: 1} |

<details close>
<summary><b>Python Solution</b></summary>

```python
# Read the input data
n = int(input("Enter an integer: "))

# Generate the dictionary with keys from 1 to n and values as squares of keys
squares_dict = {i: i**2 for i in range(1, n + 1)}

# Print the dictionary
print(squares_dict)
```
</details>


<!-- 516 -->
## Example 2: Character Count in String - Easy 😊 (Est. Time: 10 mins | Points: 10)

**Problem:** Write a program to create a dictionary from an input string to count the number of occurrences of each character.

| No. | Inputs                    | Outputs                                                          |
| --- | ------------------------- | ---------------------------------------------------------------- |
| 1   | Lorem ipsum dolor sit amet | {'L': 1, 'o': 3, 'r': 2, 'e': 2, 'm': 3, ' ': 4, 'i': 2, 'p': 1, 's': 2, 'u': 1, 'd': 1, 'l': 1, 't': 2, 'a': 1} |
| 2   | Hello World               | {'H': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'W': 1, 'r': 1, 'd': 1} |
| 3   | Python is fun             | {'P': 1, 'y': 1, 't': 1, 'h': 1, 'o': 1, 'n': 2, ' ': 2, 'i': 1, 's': 1, 'f': 1, 'u': 1} |
| 4   | Data Science              | {'D': 1, 'a': 2, 't': 1, ' ': 1, 'S': 1, 'c': 2, 'i': 1, 'e': 2, 'n': 1} |

<details close>
<summary><b>Python Solution</b></summary>

```python
# Read the input data
input_data = input("Enter a string: ")

# Create a dictionary to count the occurrences of each character
char_count = {}
for char in input_data:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1

# Print the dictionary
print(char_count)
```
</details>

<!-- 536 -->
## Example 3: Count Unique Values in List - Easy 😊 (Est. Time: 10 mins | Points: 10)

**Problem:** Given a list of integers, determine the number of unique values.

| No. | Inputs                | Outputs               |
| --- | --------------------- | --------------------- |
| 1   | 1 3 4 5 6 5 1 9       | 6                     |
| 2   | 2 2 2 2 2             | 1                     |
| 3   | 7 8 9 10 11           | 5                     |
| 4   | 3 1 4 1 5 9           | 5                     |

<details close>
<summary><b>Python Solution</b></summary>

```python
# Read the input data
input_data = input("Enter a string: ")

# Create a dictionary to count the occurrences of each character
char_count = {}
for char in input_data:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1

# Print the number of elements
print(len(char_count))
```
</details>


<!-- 543 -->
## Example 4: Word Frequency Count - Medium 🔥 (Est. Time: 10-15 mins | Points: 20)

**Problem:** Write a program to count the frequency of words in the given sentence. The output should be in reverse alphanumeric order.

| No. | Inputs                               | Outputs                              |
| --- | ------------------------------------ | ------------------------------------ |
| 1   | The five boxing wizards jump quickly | wizards: 1<br>quickly: 1<br>jump: 1<br>five: 1<br>boxing: 1<br>The: 1 |
| 2   | She sells sea shells by the sea shore | shore: 1<br>shells: 1<br>the: 1<br>sea: 2<br>she: 1<br>sells: 1<br>by: 1 |
| 3   | Peter Piper picked a peck of pickled peppers | peppers: 1<br>pickled: 1<br>peck: 1<br>Piper: 1<br>picked: 1<br>Peter: 1<br>a: 1<br>of: 1 |
| 4   | A quick brown fox jumps over the lazy dog | the: 1<br>quick: 1<br>over: 1<br>lazy: 1<br>jumps: 1<br>fox: 1<br>dog: 1<br>brown: 1<br>A: 1 |

<details close>
<summary><b>Python Solution</b></summary>

```python
# Read the input data
input_data = input("Enter a sentence: ")

# Split the input data into a list of words
words = input_data.split()

# Create a dictionary to store the frequency of each word
word_freq = {}
for word in words:
    if word in word_freq:
        word_freq[word] += 1
    else:
        word_freq[word] = 1

# Sort the dictionary by keys in reverse alphanumeric order
sorted_word_freq = sorted(word_freq.items(), key=lambda x: x[0], reverse=True)

# Print the result
for word, freq in sorted_word_freq:
    print(f"{word}: {freq}")
```
</details>

