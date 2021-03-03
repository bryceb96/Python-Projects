#this program is a two player Rock-Paper-Scissors game. This program first asks each player for rock, paper, or scissors and decides the player that wins based off of those choices.
#program will then ask if players want to play another game.
validate = True

while validate == True:
    player1 = str(input("player1 choose a option: rock paper or scissors "))
    player2 = str(input("player2 choose an option: rock paper or scissors "))

    if player1 == "rock" and player2 == "paper":
        print("player2 wins!")
        answer = str(input("do you want to play another game?"))
        if answer == "yes":
            validate = True
            continue
        else:
           validate = False
           break

    elif player1 == "rock" and player2 == "scissors":
        print("player1 wins!")
        answer = str(input("do you want to play another game?"))
        if answer == "yes":
            validate = True
            continue
        else:
            validate = False
            break
    elif player1 == "rock" and player2 == "rock":
        print("Issa tie, play again")
        answer = str(input("do you want to play another game? "))
        if answer == "yes":
            validate = True
            continue
       
        else:
            validate = False
            break
    elif  player1 == "paper" and player2 == "rock":
        print("player1 wins!")
        answer = str(input("do you want to play another game?"))
        if answer == "yes":
            validate = True
            continue
        else:
            validate = False
            break
    
    elif player1 == "paper" and player2 == "scissors":
        print("player2 wins!")
        answer = str(input("do you want to play another game?"))
        if answer == "yes":
            validate = True
            continue
        else:
            validate = False
            break
        
    elif player1 == "paper" and player2 == "paper":
        print("its a tie, play again") 
        validate = True
        continue

    elif player1 == "scissors" and player2 == "paper":
        print("player1 wins!")
        answer = str(input("do you want to play another game?"))
        if answer == "yes":
            validate = True
            continue
        else:
            validate = False
            break
        
    elif player1 == "scissors" and player2 == "rock":
        print("player2 wins!")
        answer = str(input("do you want to play another game?"))
        if answer == "yes":
            validate = True
            continue
        else:
            validate = False
            break
        
    elif player1 == "scissors" and player2 == "scissors":
        print("its a tie, play again")
        answer = str(input("do you want to play another game?"))
        if answer == "yes":
            validate = True
            continue
        else:
            break


