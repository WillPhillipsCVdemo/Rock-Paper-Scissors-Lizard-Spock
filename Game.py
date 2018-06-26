from random import choice
# List of play options
options = ['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock']

outcomes = {
    ('Scissors', 'Paper'): 'cuts',
    ('Paper', 'Rock'): 'covers',
    ('Rock', 'Lizard'): 'crushes',
    ('Lizard', 'Spock'): 'poisons',
    ('Spock', 'Scissors'): 'smashes',
    ('Scissors', 'Lizard'): 'decapitates',
    ('Lizard', 'Paper'): 'eats',
    ('Paper', 'Spock'): 'disproves',
    ('Spock', 'Rock'): 'vaporizes',
    ('Rock', 'Scissors'): 'crushes'
}

play = True

while play == True:

    computer = choice(options)
    user_input = input('Please select; Rock, Paper, Scissors, Lizard or Spock\n')
    player = user_input.lower().capitalize()

    # Makes sure that player makes valid choice
    while player not in options:
        player = input('Please select; Rock, Paper, Scissors, Lizard or Spock\n')

    print(f'Player: {player}')
    print(f'Computer: {computer}')

    if (player, computer) in outcomes:
        print(f'You win! {player} {outcomes[player, computer]} {computer}.')
    elif (computer, player) in outcomes:
        print(f'You lose! {computer} {outcomes[computer, player]} {player}.')
    else:
        print('Tie!')  

    print('Would you like to play again? (Y/N)')
    answer = input()

    if answer.lower() =='y' or answer.lower() =='yes':
        play == True
    else:
        break
