'''
Asks the user for a name, after that, the user have to guess
in six steps which number the computer "thought" of.
'''

import random   # imports the random module

guesses_taken = 0   # inits the 'guesses_taken' variable

print('Hello! What is your name?')  # prints welcome message, asks for name
myName = input()    # waiting for input, assigning input to variable 'myName'

number = random.randint(1, 20)  # assign a random number (between 1 and 20) to a variable 'number'
print('Well, ' + myName + ', I am thinking of a number between 1 and 20.')  # prints informative message

while guesses_taken < 6:    # a loop while 'guesses_taken' variable is lower than 6
    print('Take a guess.')  # prints a message asking for input
    guess = input()         # waiting for input, assigning input to variable 'guess'
    guess = int(guess)      # converts the input to an integer, and reassign it to variable 'guess'

    guesses_taken += 1      # increments the 'guesses_taken' variable by one

    if guess < number:      # tests if the condition is true: the user's input is lower than the generated number
        print('Your guess is too low.')     # if true, prints informative message

    if guess > number:      # tests if the condition is true: the user's input is higher than the generated number
        print('Your guess is too high.')    # if true, prints informative message

    if guess == number:     # tests if the condition is true: the user's input is equal to the generated number
        break   # if true, breaks the while cycle

if guess == number:     # tests if the condition is true: the user's input is equal to the generated number
    guesses_taken = str(guesses_taken)  # converts the 'guesses_taken' variable to a string, and reassign it
    print('Good job, ' + myName + '! You guessed my number in ' + guesses_taken + ' guesses!')  # prints message

if guess != number:     # tests if the condition is true: the user's input is NOT equal to the generated number
    number = str(number)    # convert the random generated number to a string and reassign it
    print('Nope. The number I was thinking of was ' + number)   # prints informative message
