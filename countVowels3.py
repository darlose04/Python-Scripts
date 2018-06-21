def count_vowels():

    mystr = input('Enter a string: ')
    count_a = mystr.lower().count('a')
    count_e = mystr.lower().count('e')
    count_i = mystr.lower().count('i')
    count_o = mystr.lower().count('o')
    count_u = mystr.lower().count('u')
    total = count_a + count_e + count_i + count_o + count_u
    
    print('total vowels: {}'.format(total))

count_vowels()
