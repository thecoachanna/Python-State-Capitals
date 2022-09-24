# from capitals import states
from capitals import states
import random

# random.shuffle(states)
random.shuffle(states)


# while True:
user_name = input("Enter your name: ")
    # if name.lower() == 'matt':
    #     break

# welcome_msg = f"Start the game now, {name}"
welcome_msg = (f'Welcome, {user_name}! You can now start the game!')

# print(welcome_msg)
print(welcome_msg)

def play_game():
    correct = 0
    incorrect = 0

    for state in states:
   
        prompt = input(f"What is the capital of {state['name']}? ")

        if state['capital'] == prompt:
            print('That is correct!')
            correct += 1
        else: 
            print('That is incorrect.')
            incorrect += 1
    
        if correct + incorrect == 50:
            retry = input('Would you like to play again? Y/N ')
            if retry == 'Y' or retry == 'y':
                play_game() 
            else:
                break
            return

play_game()


