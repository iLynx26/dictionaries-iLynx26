normal_alphabet = input()
encryption_alphabet = input()

to_be_encrypted = input()
encrypted = ""
to_be_decrypted = input()
decrypted = ""

for letter in to_be_encrypted:
    j = normal_alphabet.find(letter)
    encrypted += encryption_alphabet[j]

print(encrypted)

for letter in to_be_decrypted:
    j = encryption_alphabet.find(letter)
    decrypted += normal_alphabet[j]
print(decrypted)


# #d#%#d###d#
# bada

"""
Напишіть програму, яка вміє шифрувати і розшифровувати використовуючи abcd
1234
ababcdcd
44332211шифр підстановки. 
Програма приймає на вхід два рядки однакової довжини, у першому рядку записані символи початкового алфавіту, 
у другому рядку - символи кінцевого алфавіту (шифр підстановки), після чого йде рядок, 
який потрібно зашифрувати переданим шифром підстановки, і ще один рядок, який потрібно розшифрувати. 
Нехай, наприклад, на вхід програми передано:

abcd
*d%#
abacabadaba
#*%*d*%
Це означає, що символ 
a вхідного повідомлення замінюється на символ * в шифрі, 
b замінюється на d, 
c - на % і 
d - на #. 

Потрібно зашифрувати рядок abacabadaba і розшифрувати рядок 
#*%*d*% за допомогою цього шифру. 
# 
# Отримуємо наступні рядки, які і передаємо на виведення програми:

*d*%*d*#*d*
dacabac

Вхідні дані:

abcd
1234
ababcdcd
44332211
Вихідні дані:

12123434
ddccbbaa
"""