print("Welcome to the game HangMan!")
word = "print"
wrong_count = 0
guess_chars = set()
word_chars = set(word)

def check_char(guess_chars, wrong_count, word_chars):
    if guess in word_chars:
        print("You're reight! Let's move on to the next letter!")
        guess_chars.add(guess)
    else:
        print("You're wrong. You lose on life")
        wrong_count += 1

while wrong_count < 6:
    while not guess_chars == word_chars:
        guess = input("Please enter your guess: ")
        check_char(guess_chars, wrong_count, word_chars)
