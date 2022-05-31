"""
    Welcome come to the rock paper scissor game
    where you will be given an input to put the corresponding value 
    R for rock
    P for paper
    S for scissors
"""
from random import choice

instructions = f"Welcome come to the rock paper scissor game!!!.\n Please insert the correct value for this game \n R for Rock \n P for Paper  \n S for Scissors"
print(instructions)

winner = True

while winner:
    user = str(input('pick between rock paper and scissors: '))
    player = user.upper()
    computer = ['R','P','S']
    computers_choice = choice(computer)
    
    # login
    if player=='R' or player=='P' or player=='S':

        if player =='R' and computers_choice =='P':
            print(f'Player {player} : CPU {computers_choice}')
            print('CPU wins')
            winner=False
        
        elif player =='P' and computers_choice == 'R':
            print(f'Player {player} : CPU {computers_choice}')
            print('Player wins!')
            winner = False

        elif player=='R' and computers_choice =='S':
            print(f'Player {player} : CPU {computers_choice}')
            print("Player wins!")
            winner = False

        elif player=='P' and computers_choice =='S':
            print(f'Player {player} : CPU {computers_choice}')
            print("CPU wins!")
            winner = False

        elif player=='S' and computers_choice =='R':
            print(f'Player {player} : CPU {computers_choice}')
            print("CPU wins!")
            winner = False

        elif player=='S' and computers_choice =='P':
            print(f'Player {player} : CPU {computers_choice}')
            print("Player wins!")
            winner = False
            
        else:
            print(f"It's a draw! Play again")     
    else:
        print('invalid value please try again')