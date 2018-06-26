# Write a program that prints the longest substring of s in which the letters
# occur in alphabetical order.
# For example, if s = ''azcbobobegghakl', then your program should print:
# longest substring in alphabetical order is: beggh
# In the case of ties, print the first substring.
# For example, if s = 'abcbcd', then the program should print:
# longest substring in alphabetical order is: abc

s = 'ufackorvnjejww'
longest = s[0]
current = s[0]

for c in s[1:]:            # checking the characters in s beginning with 'z'
    if c >= current[-1]:   # if the character c is greater than (alphabetically next) the
        current += c       # last character in the variable current ([-1]), add it to current
        if len(current) > len(longest): # if current becomes longer than longest,
            longest = current           # it becomes the variable longest
    else:
        current = c
print('The longest substring in alphabetical order is: {}'.format(longest))
