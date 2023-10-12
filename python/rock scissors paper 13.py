import random

choices = ["rock", "paper", "scissors"]
again = True

while again:
    try:
        player = input("Enter rock, paper, or scissors: ").lower()
        if player not in choices:
            print("Only enter rock, paper, or scissors!!!")
            continue 

        computer = random.choice(choices)       
       
        print("Player:", player)
        print("Computer:", computer)

        if player == computer:
            print("It's a tie")
        elif (player == "rock" and computer == "scissors") or (player == "paper" and computer == "rock") or (player == "scissors" and computer == "paper"):
            print("player wins!!")
        else:
            print("computer wins!!")

        answer = input("Do you want to play again?? (Y/N)").upper()
        if answer == "Y":
            continue
        else:
            again = False
            
    except ValueError as e:
        print(e)

