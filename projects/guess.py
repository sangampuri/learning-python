import random


def play_game():
    computerChoice = random.randint(1,10)
    userGuess = None
    count_attempts = 0


    while  userGuess != computerChoice:
        count_attempts +=1
        userGuess = int(input('Guess the number : '))


        if userGuess > computerChoice:
            print('Too high!')
            

        elif userGuess < computerChoice:
            print('Too low!')


    print(f'Congratulations!. You guessed the number in {count_attempts} attempts.')

    user_decision = input('Do you want to play again? (yes/no):')
    user_decision = user_decision.strip().lower()
    return user_decision

user_decision = 'yes'
print(user_decision)

while user_decision == 'yes':
    user_decision = play_game()

print('Thanks for playing')
print(user_decision)
