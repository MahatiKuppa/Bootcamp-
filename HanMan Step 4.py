# TODO - 1: create a variable called lives and keep a track of the six lives of hangman
# TODO - 2: if guess is not a letter in chosen word, then the lives is reduced by 1 and if lives go down to 0, then the game should stop and it shuold say "You lose"
# TODO - 3: print the ascii art from "stages" corresponding to the number of lives remaining

stages = [
    """
       +---+
       |   |
           |
           |
           |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
           |
           |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
       |   |
           |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
      /|   |
           |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
      /|\\  |
           |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
      /|\\  |
      /    |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
      /|\\  |
      / \\  |
           |
    =========
    """
]


word_list = ["aardvark", "baboon", "camel"]
import random
chosen_word = random.choice(word_list)
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

    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            print("Uh-oh! You lose")
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
    print(stages[6 - lives])
    print(display)



        


