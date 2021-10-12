import random
import time


n = int(input('Enter a num between 1 and: '))
number = random.randint(1,n)
guess = int(input('Enter a number between 1 and {} : '.format(n)))

while guess != number:
    if guess < number:
        print('Your guess was low')
        time.sleep(1)
        guess = int(input('Enter a number between 1 and {} : '.format(n)))

    if guess > number:
        print('Your guess was high')
        time.sleep(1)
        guess = int(input('Enter a number between 1 and {} : '.format(n)))

print('You guessed it!')