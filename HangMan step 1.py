# TODO: Randomly choose a word from the word_list and assign it to a variable called "chosen_word"
# TODO: Ask the user to guess a letter and assign the answer to a variable called guess. Make guess lowercase
# TODO: Check if the letter matches with guess and is one of the letters in the chosen_word. Print "Right" if it matches, "Wrong" if it doesn't.

word_list = ["aardvark", "baboon", "camel"]
import random
chosen_word = random.choice(word_list)
print(chosen_word)
guess = (input("Guess a letter: ")).lower()
print(guess)
for char in chosen_word:
    if char == guess:
        print("Right")
    else:
        print("Wrong")
