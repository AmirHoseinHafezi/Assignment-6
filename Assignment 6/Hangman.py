#First pip install random-word
from random_word import RandomWords
r = RandomWords()

while True:
    try:
        pre_secret_word = r.get_random_word() # Return a single random word
        secret_word = pre_secret_word.lower()
        break
    except:
        TypeError or NameError
dashes = len(secret_word)*"-"
guesses_left = 7
guessed = []
hangman = ['''
=========           
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
========='''] # Stages of hangman

def get_guess():
    while True:
        guess = input("Guess: ")
        if len(guess) != 1:
            print("Guess needs to be one character")
        elif guess.isupper():
            print("Guess needs to be lowercase")
        if guess.islower() and len(guess) == 1:
            return guess
def update_dashes(secret_word, dashes, guess):
    for i in range(len(secret_word)):
        if secret_word[i] == guess:
            dashes = dashes[:i] + guess + dashes[i+1:]
    return dashes
while (dashes != secret_word) and (guesses_left > 0):
    if guesses_left == 7:
        print(hangman[0])
    elif guesses_left == 6:
        print(hangman[1])
    elif guesses_left == 5:
        print(hangman[2])
    elif guesses_left == 4:
        print(hangman[3])
    elif guesses_left == 3:
        print(hangman[4])
    elif guesses_left == 2:
        print(hangman[5])
    elif guesses_left == 1:
        print(hangman[6])
    elif guesses_left == 0:
        print(hangman[7])
    print(dashes)
    user_guess = get_guess()
    dashes = update_dashes(secret_word,dashes,user_guess)
    if user_guess not in guessed:
        guessed.append(user_guess)
        if user_guess in secret_word:
            print("Good guess!")
            print("Letters guessed: " + str(guessed))
        else:
            print("That letter is not in the secret word.")
            guesses_left -= 1
            print("Guesses left: " + str(guesses_left))
            print("Letters guessed: " + str(guessed))
    elif user_guess in guessed:
        print("You already guessed this character bro")
        print("Guesses left: " + str(guesses_left))
        print("Letters guessed: " + str(guessed))
if dashes == secret_word: # Winner Ending
    print(dashes)
    print("")
    print("You win!")
    print("Bro is a glorious guesser :O")
    print("The word was: " + secret_word)
elif guesses_left == 0: # Loser Ending ;-;
    print("")
    print("You lost ;-;")
    print("Bro ran out of turns...")
    print("The word was: " + secret_word)
    print("Maybe next time?")