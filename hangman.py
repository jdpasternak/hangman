# hangman.py
# author    jake and gaby

'''
This is more of a “guess the word” game. 
The core concepts you have to use while developing this project are variables, 
random, integer, strings, char, input and output, and boolean. 
In the game, users have to enter letter guesses, and each user will have a limited number of guesses 
(a counter variable is needed for limiting the guesses). 
This is one of the interesting python projects to begin with. 

You can create a pre-organized list of words that users can grab words from. 
Also, you must include specific functions to check whether or not a user has entered a single 
letter or if the input letter is in the hidden word, to if the user has actually inputted a single letter, 
and to print the correct outcomes (letters).
'''

'''
Requirements

Variables
=========
- words
- counter

 ()
/||\\
_/\_

Flow
====
1. Randomly choose a word from a list of words
2. While counter is less than 8 AND word is incomplete
    1. Prompt for a guess
    2. If...
        a. guess is in word
            - display correct letters
        b. guess has already been guessed
            - advise user of previous guess
        c. otherwise
            - increment counter
            - draw body part
3. If...
    a. Word is complete
        - display congratulations message
    b. Counter equals 8
        - display game over message
'''

# Import
import random

# Variable Declarations
word_list = [
    'organized',
    'outcomes',
    'train',
    'kamehameha',
    'apocalypse'
]
counter = 0
prompting = True
guesses = []
hanged_man_stages = [
    ' ()\n\n',
    ' ()\n ||\n',
    ' ()\n/||\n',
    ' ()\n/||\\\n',
    ' ()\n/||\\\n /',
    ' ()\n/||\\\n_/',
    ' ()\n/||\\\n_/\\',
    ' ()\n/||\\\n_/\\_'
]
hanged_man_free = '\\()/\n ||\n_/\\_'

# Greet player with welcome message.
welcome_message = '''Welcome to Hangman! Good luck!
=============================='''
print(welcome_message)

# Randomly select word from list of words.
# 1. Randomly choose a word from a list of words
word_index = random.randint(0,4)
word = word_list[word_index]
word_as_list = list(word)

guess_word_as_list = list(len(word) * '_')
guess_word = "".join(guess_word_as_list)
print(guess_word)

# Prompt user for guess.
while ((counter <8) and not(word == guess_word)): # determine if game is still going
    print('Enter a letter to guess:')
    guess = input().lower()
    
    # check if guess is valid
    if not guess.isalpha():
        print('Enter only a letter')
    elif len(guess) > 1:
        print('Enter only ONE letter')
    elif guess in guesses:
        print('You\'ve already guessed that letter!')
    
    # guess is valid
    else:
        guesses.append(guess)
        #print(guesses)
        print('You guessed the letter \'' + guess + '\'')
        
        if guess in word:
            for i in range(0,len(word)):
                if guess == word_as_list[i]:
                    guess_word_as_list[i] = guess
                    guess_word = "".join(guess_word_as_list)
            print(guess_word)
        # word does not contain letter
        else:
            print('The word does not contain the letter \'' + guess + '\'')
            print(hanged_man_stages[counter])
            counter += 1

if (counter == 8):
    print('Game Over! Your man is hanged!')
elif (word == guess_word):
    print('Congratulations! You\'ve won the game! Your man is free!')
    print(hanged_man_free)
