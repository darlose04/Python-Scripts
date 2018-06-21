# Counts the number of words in a string
'''
string = input('Please enter a sentence: ')

words = string.split(" ")
print(len(words))
'''

def countWords(string):

    words = string.split(" ")
    return len(words)

print(countWords("How are you?"))

