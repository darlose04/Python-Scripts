# Write a program that counts the number of vowels in a string

s = 'azcbobobegghakl'

count_a = s.lower().count('a')
count_e = s.lower().count('e')
count_i = s.lower().count('i')
count_o = s.lower().count('o')
count_u = s.lower().count('u')
total = count_a + count_e + count_i + count_o + count_u
print('Number of vowels: {}'.format(total))
