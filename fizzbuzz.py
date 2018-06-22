# Fizz Buzz
# Write a program that prints the numbers from 1 to 100.
# But for multiples of three print “Fizz” instead of the number and
# for the multiples of five print “Buzz”.
# For numbers which are multiples of both three and five print “FizzBuzz”.

def fizz_buzz():
    # creates a range of numbers from 1-101 (not inclusive)
    for num in range(0,101):
        # if the number in the range is evenly divisible by
        # 5 and 3, 'FizzBuzz' will be printed in place of the number
        if num % 5 == 0 and num % 3 == 0:
            print('FizzBuzz')
        # if number is divisible by 5, 'Buzz' will be printed
        # in its place
        elif num % 5 == 0:
            print('Buzz')
        # if number is divisible by 3, 'Fizz' will be printed
        # in its place
        elif num % 3 == 0:
            print('Fizz')
        # if the number is not divisible by 5 or 3,
        # then the number will be printed
        else:
            print(num)

fizz_buzz()
