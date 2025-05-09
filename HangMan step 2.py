# TODO - 1: create String called placeholder with the same number of blanks as chosen word
# TODO - 2: create a "display" that puts the guessed letter in the right placeholder

word_list = ["aardvark", "baboon", "camel"]
import random
chosen_word = random.choice(word_list)
print(chosen_word)
guess = (input("Guess a letter: ")).lower()
print(guess)
# for char in chosen_word:
#     if char == guess:
#         print("Right")
#     else:
#         print("Wrong")

# TODO - 1:
placeholder = ""
for char in chosen_word:
    placeholder += "_"

print(placeholder)

# TODO - 2:
display = ""
for char in chosen_word:
    if char == guess:
        display += guess
    else:
        display += "_"

print(display)


