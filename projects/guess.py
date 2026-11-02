import random

computerChoice = random.randint(1,10)
userGuess = None



while  userGuess != computerChoice:
    userGuess = int(input('Guess the number : '))


    if userGuess > computerChoice:
        print('Too high!')
        

    elif userGuess < computerChoice:
        print('Too low!')

if userGuess == computerChoice:
     print('Congratulations!')

