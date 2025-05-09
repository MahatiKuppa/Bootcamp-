# Alphabet characters (uppercase and lowercase)
alphabets = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]  # [1][2]

# Digit characters
digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']  # [3]

# Special characters
special_chars = [
    '!', '#', '$', '%', '&', '(', ')', '*', '+', '-',
    '.', ':', ';', '<', '=', '>', '?', '@', '^', '_', '|', '~']  # [4]

import random

letters = int(input("How many letters do you want in your password?"))
num_digits = int(input("How many digits do you want in your passowrd?"))
characters = int(input("How many special characters do you want in your passwords?"))

#Easy version
password_characters = []
for i in range(0,letters):
    password_characters.append(random.choice(alphabets))
for i in range(0,num_digits):
   password_characters.append(random.choice(digits))
for i in range(0, characters):
    password_characters.append(random.choice(special_chars))

easy_password = ''.join(password_characters)

print(f"Easy passowrd: {easy_password}")

random.shuffle(password_characters)

tough_password = ''.join(password_characters)
print(f"Tough password: {tough_password}")