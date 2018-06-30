# -*- coding: utf-8 -*-
"""
Created on Mon Apr 23 18:42:48 2018

@author: zsmit
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