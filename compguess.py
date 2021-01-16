import random

def guesscomp(x):
    random_number = random.randint(1,x)
    guess = 0
    while(guess != random_number):
        guess = int(input(f'Guess a Number between (1,{x}): '))
        if(guess < random_number):
            print("SorrY !! Your guess - LOW")
        elif guess >random_number:
            print("SorrY !! Your Guess - High")

    print(f'Winner Winner , Right Guess !! , Number : {random_number}')

guesscomp(1000)
