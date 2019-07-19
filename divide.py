# this is the guess number game:

import random

print("Hello what's your name?")
name  = input()

print('hello '+ name + ',would like to guess a number between 1 to 20 ? ')

secretnumber = random.randint(1,20)

for i in range(1,7):
    print('take a guess')
    guess = int(input())

    if guess < secretnumber:
        print('your guess is to low')
    elif guess > secretnumber:
        print('your guess is to high')
    elif guess == secretnumber: 
        print('Done..! '+ name + 'you got the number in' + str(i) +' guesses')
        break
    else:
        break

print('the number i was thinking ' + str(secretnumber))
