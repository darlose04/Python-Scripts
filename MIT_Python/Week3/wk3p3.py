# -*- coding: utf-8 -*-
"""
Problem 3 - Printing Out all Available Letters

Next, implement the function getAvailableLetters that takes in one parameter - a list of letters, lettersGuessed. 
This function returns a string that is comprised of lowercase English letters - all lowercase English letters that are not in lettersGuessed.
"""

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    import string
    alphabet = list(string.ascii_lowercase)
    available_letters = []
    for item in alphabet:
        if item not in lettersGuessed:
            available_letters.append(item)
    return ''.join(available_letters)
