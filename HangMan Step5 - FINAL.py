# TODO -1 : update word_list to use 'word list' from hangman.py - DONE
# TODO -2 : Update the code to use the stages list from hangman_art.py - DONE
# TODO -3 : Import the logo from hangman_art.py and print it at the start of the game - DONE
# TODO -4 : if the user has already guessed a letter, let hem know -
# TODO -5 : If the guess is not in the word, print out that letter and let the user know - DONE
# TODO -6 : Update the code to tell the user how many lives they have left - DONE
# TODO -7 : Update the print statement in the end to give the user the correct output - DONE

import hangman
import hangman_art
import random
chosen_word = random.choice(hangman.word_list)
print(chosen_word)

placeholder = ""
for char in chosen_word:
    placeholder += "_"
print(placeholder)

correct_letters = []
lives = 6
display = ""



while display != chosen_word:
    guess = input("Guess a letter: ").lower()
    if guess in correct_letters:
        print("You have already guessed this letter")
    if guess not in chosen_word:
        lives -= 1
        print(f"You chose {guess}. That is not there in the word :(")
        print(f"{lives} Lives left!")
        if lives == 0:
            print("****************YOU LOSE****************")
            print(f"The correct word is {chosen_word}")
    else:
        display = ""
        for letter in chosen_word:
            if letter == guess:
                display += letter
                correct_letters.append(guess)
            elif letter in correct_letters:
                display += letter
            else:
                display += "_"
    print(hangman_art.stages[6 - lives])
    print(display)

print("****************YOU WIN****************")