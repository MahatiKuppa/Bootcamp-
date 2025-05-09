# TODO - 1: Use a while loop to let the user guess again
# TODO - 2: change the for loop so that we keep the previous correct guess and add the new ones.

word_list = ["aardvark", "baboon", "camel"]
import random
chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
for char in chosen_word:
    placeholder += "_"

print(placeholder)

display = placeholder
while display != chosen_word:
    guess = (input("Guess a letter: ")).lower()
    for i in range(0,len(chosen_word)):
        guess_list = list(display)
        if chosen_word[i] == guess:
            guess_list[i] = guess
        display = "".join(guess_list)
    print(display)




    #or

word_list = ["aardvark", "baboon", "camel"]
import random
chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
for char in chosen_word:
    placeholder += "_"

correct_letters = []

while display != chosen_word:
    guess = input("Guess a letter: ").lower()
    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"
