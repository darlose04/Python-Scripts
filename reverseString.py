# Reverse a String
# Enter a string and the program will reverse it and print it out.

def reverse_string():

    word = str(input('Enter a string: '))
    word_reverse = word[::-1]
    print(word_reverse)
    
reverse_string()
