def count_vowels():

    mystr = input('Enter a string: ')

    print('a: {}'.format(mystr.lower().count('a')),
    'e: {}'.format(mystr.lower().count('e')),
    'i: {}'.format(mystr.lower().count('i')),
    'o: {}'.format(mystr.lower().count('o')),
    'u: {}'.format(mystr.lower().count('u')))

count_vowels()
