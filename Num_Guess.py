import random

start = input('Want to play a game?\n(yes / no) : ')

if start == 'yes':
    name = input('I need to know your name, if you want to play: ')
elif start == 'no':
    print('Thank you, GOOD BYE! ')
    quit()
else:
    print('Invalid input, GOOD BYE!')
    quit()

# Initializing bounds
a = 0
b = 21

# script gaining the random number
numb = (random.uniform(a, b)//1)

# guess checker
while a != numb:
    num1 = int(input('Enter in a number''\nHINT: Under 20 : '))
    a = num1
    if a == numb :
        print('YOU DID IT, YOU GUESSED MY NUMBER ' + name.upper() + '!')
        quit()
    if a > numb :
        print('Price is Right Rules, You Lost! Try Again  ')

    else:
        print('Your number fell short of the mark, Try Again')

