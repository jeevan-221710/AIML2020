#Nine lives
import random
lives = 9
heart_symbol = '\u2764'
words = ["hello","pizza","apple","fairy","teeth"]
secret_word = random.choice(words)
clue = list('?????')
guessed_word_correctly = False
def update_clue(guessed_letter,secret_word,clue):
    index = 0
    while index<len(secret_word):
        if guessed_letter == secret_word[index]:
            clue[index] = guessed_letter
        index += 1           
while lives>0:
    print(clue)
    print("lives left:",heart_symbol*lives)
    guess = input("Guess a letter or whole word: ")
    if guess == secret_word:
        guessed_word_correctly = True
        break
    elif guess in secret_word:
        update_clue(guess,secret_word,clue)
    else:
        print("Incorrect guess.you lose a life")
        lives -= 1
if guessed_word_correctly==True:
    print("You won the game,Secret_word was:",secret_word)
else:
    print("You lost the game,Secret_word was:",secret_word)
['?', '?', '?', '?', '?']
lives left: ❤❤❤❤❤❤❤❤❤
Guess a letter or whole word: t
Incorrect guess.you lose a life
['?', '?', '?', '?', '?']
lives left: ❤❤❤❤❤❤❤❤
Guess a letter or whole word: f
Incorrect guess.you lose a life
['?', '?', '?', '?', '?']
lives left: ❤❤❤❤❤❤❤
Guess a letter or whole word: a
Incorrect guess.you lose a life
['?', '?', '?', '?', '?']
lives left: ❤❤❤❤❤❤
Guess a letter or whole word: e
['?', 'e', '?', '?', '?']
lives left: ❤❤❤❤❤❤
Guess a letter or whole word: l
['?', 'e', 'l', 'l', '?']
lives left: ❤❤❤❤❤❤
Guess a letter or whole word: o
['?', 'e', 'l', 'l', 'o']
lives left: ❤❤❤❤❤❤
Guess a letter or whole word: h
['h', 'e', 'l', 'l', 'o']
lives left: ❤❤❤❤❤❤
