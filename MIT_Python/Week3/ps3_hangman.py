# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functionbs
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "words.txt"


def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print(len(wordlist), "words loaded.")
    return wordlist


def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------


# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()


def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    secret_word_list = list(secretWord)
    return set(secret_word_list).issubset(lettersGuessed)


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    secret_word_list = list(secretWord)
    guessed_word_list = []
    for item in secret_word_list:
        if item in lettersGuessed:
            guessed_word_list.append(item)
        else:
            guessed_word_list.append('_ ')
    return ''.join(guessed_word_list)


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''

    alphabet = list(string.ascii_lowercase)
    available_letters = []
    for item in alphabet:
        if item not in lettersGuessed:
            available_letters.append(item)
    return ''.join(available_letters)


def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the
      partially guessed word so far, as well as letters that the
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''

    print('Welcome to the game, Hangman!')
    print('I am thinking of a word that is {} letters long.'.format(len(secretWord)))
    print('-------------')

    guesses_left = 8
    lettersGuessed = []

    # iterates through user guesses
    # determines if guess is correct or not
    # returns if user wins or loses
    while guesses_left > 0:

        print('You have {} guesses left.'.format(guesses_left))
        print('Available letters: {}'.format(getAvailableLetters(lettersGuessed)))
        guess = str(input('Please guess a letter: ')).lower()

        if guess in secretWord:
            if guess in lettersGuessed:
                print("Oops! You've already guessed that letter: {}".format(
                    getGuessedWord(secretWord, lettersGuessed)))
                print('------------')
                continue
            lettersGuessed.append(guess)
            print('Good guess: {}'.format(getGuessedWord(secretWord, lettersGuessed)))
            print('------------')

            if isWordGuessed(secretWord, lettersGuessed) == True:
                print('Congratulations, you won!')
                break
            else:
                continue

        elif guess in lettersGuessed:
            print("Oops! You've already guessed that letter: {}".format(
                getGuessedWord(secretWord, lettersGuessed)))
            print('------------')

        elif guess not in secretWord:
            print('Oops! That letter is not in my word: {}'.format(
                getGuessedWord(secretWord, lettersGuessed)))
            print('------------')
            guesses_left -= 1
            lettersGuessed.append(guess)

            if guesses_left == 0:
                print('Sorry, you ran out of guesses. The word was {}.'.format(secretWord))
                break

# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)


secretWord = chooseWord(wordlist).lower()
#secretWord = 'secret'
hangman(secretWord)
