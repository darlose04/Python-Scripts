# A program to check if the string entered by a user
# is a palindrome or not.

user_string = input('Please enter a string: ')

if user_string[::1] == user_string[::-1]:
    print('This is a palindrome!')
else:
    print('This is not a palindrome!')
