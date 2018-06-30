import random

def guess_num():

    print('Hello! What is your name?')
    name = str(input())

    num = random.randint(1,20)

    print('Well, ' + name + ', I am thinking of a number between 1 and 20.')
    print('You have 5 chances to correctly guess what I am thinking!')

    guesses = 1

    while True:
        guess = input()
        guess = int(guess)
        if guesses == 5:
            print('You have run out of guesses!')
            break
        elif guess < num:
            print('Your guess is too low.')
            guesses += 1
        elif guess > num:
            print('Your guess is too high.')
            guesses += 1
        elif guess == num:
            guesses += 1
            print("Good job, " + name + "! You guessed the number in {} guesses!".format(guesses-1))
            break

guess_num()