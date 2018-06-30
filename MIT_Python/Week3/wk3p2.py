# -*- coding: utf-8 -*-
"""
Problem 2 - Printing Out the User's Guess

Next, implement the function getGuessedWord that takes in two parameters - a string, secretWord, and a list of letters, lettersGuessed. 
This function returns a string that is comprised of letters and underscores, based on what letters in lettersGuessed are in secretWord. 
This shouldn't be too different from isWordGuessed!
"""

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
