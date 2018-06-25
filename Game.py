from random import randint
# create a list of play options
options = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]

play = True

while play == True:

    computer = options[randint(0, 4)]
    user_input = input("Please select; Rock, Paper, Scissors, Lizard or Spock\n")
    u = user_input.lower()

    player = u.capitalize()

    print("Player: ", player)
    print("Computer: ", computer)

    ##Tie
    if player == computer:
        print("Tie!")

    ##Rock
    elif player =="Rock":
        if computer == "Paper":
            print("You lose!", computer, "covers", player)
        elif computer == "Scissors":
            print("You win!", player, "smashes", computer)
        elif computer == "Lizard":
            print("You win!", player, "crushes", computer)
        elif computer == "Spock":
            print("You lose!", computer, "vaporizes", player)


    ##Paper
    elif player =="Paper":
        if computer == "Scissors":
            print("You lose!", computer, "cuts", player)
        elif computer =="Rock":
            print("You win!", player, "covers", computer)
        elif computer == "Lizard":
            print("You lose!", computer , "eats", player)
        elif computer == "Spock":
            print("You win!", player, "disproves", computer)

    ##Scissors
    elif player == "Scissors":
        if computer == "Paper":
            print("You win!", player, "cuts", computer)
        elif computer == "Rock":
            print("You lose!", computer, "crushes", player)
        elif computer =="Lizard":
            print("You win!", player, "decapitates", computer)
        elif computer == "Spock":
            print("You lose!", computer, "smashes", player)

    ##Lizard
    elif player == "Lizard":
        if computer =="Rock":
            print("You lose!", computer, "crushes", player)
        elif computer =="Paper":
            print("You win!", player, "eats", computer)
        elif computer == "Scissors":
            print("You lose!", computer, "decapitates", player)
        elif computer == "Spock":
            print("You win!", player, "", computer)

    ##Spock
    elif player == "Spock":
        if computer == "Rock":
            print("You win!", player, "vaporizes", computer)
        elif computer == "Paper":
            print("You lose!", computer, "disproves", player)
        elif computer == "Scissors":
            print("You win!", player, "smashes", computer)
        elif computer == "Lizard":
            print("You lose!", computer, "poisons", player)


    print("Would you like to play again? \n")
    answer =input()

    if answer.lower() =="y" or answer.lower() =="yes":
        play == True
    else:
        break