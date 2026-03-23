import random

def get_player_name():
    name = input('Hello what is your name: ')
    return name
    
def get_guess(name):
    try: 
        guess = int(input(f'Well {name}, am thinking of a number ' + '\n' + f'between 1-20, take a guess: '))
    except ValueError:
        print('Enter numbers only, Try Again')
        return get_guess(name)
    return guess

def check_guess(guess, secret):
    if guess > secret:
        return 'high'
    if guess < secret:
        return 'low'
    if guess == secret:
        return 'correct'
    
name = get_player_name()
secret = random.randint(1,20)
tries = 0
result = None

for i in range(6):
    while True:
        try:
            if result == 'high':
                guess = int(input('Too high, go a little lower, Try again: '))
            elif result == 'low':
                guess = int(input('Too low go a little higher, Try again: '))
            else:
                guess = get_guess(name)
            break
        except ValueError:
            print('Enter numbers only, Try Again')
    
    tries = tries + 1 
    result = check_guess(guess, secret)
       
    if result == 'correct':
        print(f'Good Job {name}, you guessed my number in {tries} tries ') 
        break   

if result != 'correct':
    print(f'You lost!, the number was {secret}')
