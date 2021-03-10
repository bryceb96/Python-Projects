def determine_winner(matrix):
    winner_found = False
    for i in range(0,3):
        if matrix[i][0] == matrix[i][1] == matrix[i][2]:
            if matrix[i][0] == "x":
                winner_found = True
                print("player 1 wins horizontally")
                break
            elif matrix[i][0] == "o":
                print("player 2 wins horizontally")
                winner_found = True
                break
            else:
                #print("there is no winner")
                winner_found = False
            break
        #checking horizontal columns
        elif matrix[0][i] == matrix[1][i] == matrix[2][i]:
            if matrix[0][i] == "x":
                print("player 1 wins vertically")
                winner_found = True
                break
            elif matrix[0][i] == "o":
                winner_found = True
                print("player 2 wins vertically")
                break
            else:
                winner_found = False
                #print("there is no winner")
            break
        #checking diagonally
        elif matrix[0][0] == "o" and matrix[1][1] == "o" and matrix[2][2] == "o" or matrix[0][2] == "o" and matrix[1][1] == "o" and matrix[2][0] == "o":
            print("player 2 wins diagonally")
            winner_found = True
            break
        elif matrix[0][0] == "x" and matrix[1][1] == "x" and matrix[2][2] == "x" or matrix[0][2] == "x" and matrix[1][1] == "x" and matrix[2][0] == "x":
            print("player 1 wins diagonally")
            winner_found = True
            break
    else:
       #print("there is no winner")
       winner_found = False
    return winner_found

def print_board(board): #prints the list of lists in a tic tac toe format
    [print(i) for i in board]

def extract_input(player_input): #takes in player inputs and converts the string to integer, thereby getting the plotting coordinates.
    
    coordinates = []
    player_input = player_input.split(",")
    for i in player_input:
        i = i.strip()
        i = int(i)
        coordinates.append(i)
    #for the first i, that is the row. then second iteration of i is the column. with this, it will now be easy to take in the numbers.
    return(coordinates)

def check_board(board): #check the board to see if full
    full = False #bool value
    for i in range(0,3):
        #for the entire range of the board, will check vertically and horizontally simutaenously for any open spaces.
        #if there are, bool full is False.
        #If not, bool full is True
        #return either way.

        if board[i][0] == 0 or board[i][1] == 0 or board[i][2] == 0 and board[0][i] == 0 or board[1][i] == 0 or board[2][i] == 0:
            full = False
        else:
            full = True
    return full


if __name__ == "__main__":
    #first create 3x3 table with functions from Lesson24 main
    game_board = [[0, 0, 0],
                [0, 0, 0],
                [0, 0, 0]]

    #explain rules to user 
    print("First player is x and Player 2 is o.\n For those unfamiliar, please input the position you want to move as row, column. AKA say a number for the row, a comma, and then another number for the column.\n")
    print("Do not try and put a piece where a piece already exists.\n The rows start at row 1 and go until row 3, same with columns.")
    print("Player 1 goes first, then player 2. This will repeat until the board is full.")
    print("Example: player 1 inputs (2,2)\n This comes out as: ")
    print("[0,0,0]")
    print("[0,x,0]")
    print("[0,0,0]")

    print("-----------------------------")
    print("Game start!\n")

    print_board(game_board)
    full_board = check_board(game_board)
    winner_found = determine_winner(game_board)
    game_board_range = 1000

    #full_board != True
    while winner_found != True:  
        while game_board_range != 0:
            #every time the game board range decrements, will switch to other player.
            #Player 1 == even, Player 2 == odd
            if game_board_range % 2 == 0:
                player = 1
            else:
                player = 2
            player_turn = input("Player {}, Enter the coordinates as row, column please: \n".format(player))
            coordinates = extract_input(player_turn)
            row, column = coordinates[0] - 1, coordinates[1] - 1

            if game_board[row][column] != 0:
                print("that space has already been selected, pick another spot")
                #do not decrement the game turn, allow player to go again DONE
            else:
            #check for which player is selecting and if that spot is already occupied. if game_board[row][column] != 0, go back to selecting the row and column DONE
                if player == 1:
                    game_board[row][column] = "x"
                else:
                    game_board[row][column] = "o"

                print_board(game_board)
                full_board = check_board(game_board)
                winner_found = determine_winner(game_board)
                #print(winner_found)
                #displaying then checking board to see if there are any empty spaces left. DONE
                #if there are, keep playing and decrement the board range by 1. If not, game is automatically over. Display board. DONE
                if full_board == True:
                    print("The board is full. The game has ended.")
                    determine_winner(game_board)
                    print("Thanks for playing!\n")
                    break
                elif winner_found == True:
                    print("Thanks for playing!")
                    break
                else:
                    game_board_range -= 1
                    continue
        break
            
                
    
