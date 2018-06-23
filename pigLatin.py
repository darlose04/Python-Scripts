'''
Pig Latin
Pig Latin is a game of alterations played on the English language.
To create the Pig latin form of an English word, the initial consonant
sound is transposed to the end of  the word and an ay is affixed.abs
(Ex.: "banana" would yield anana-bay)
'''

def pig_latin():

    word = str(input("Enter a word: "))
    print(word[1:] + '-' + word[0] + 'ay')

pig_latin()