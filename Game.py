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

while play is True:

    computer = choice(options)
    roll = input('Please select; Rock, Paper, Scissors, Lizard or Spock\n')
    roll = roll.lower().capitalize()

    # Makes sure that player makes valid choice
    while roll not in options:
        roll = input('Please select; Rock, Paper, Scissors, Lizard or Spock\n')

    print(f'Player: {roll}')
    print(f'Computer: {computer}')

    if (roll, computer) in outcomes:
        print(f'You win! {roll} {outcomes[roll, computer]} {computer}.')
    elif (computer, roll) in outcomes:
        print(f'You lose! {computer} {outcomes[computer, roll]} {roll}.')
    else:
        print('Tie!')

    print('Would you like to play again? (Y/N)')
    answer = input()

    if answer.lower() == 'y' or answer.lower() == 'yes':
        play = True
    else:
        break
