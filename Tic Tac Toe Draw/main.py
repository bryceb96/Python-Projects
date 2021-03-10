
    #determine winner at any time or when board is full. 
    #put in input sanitiation for correct format of rows and columns.

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
    print(full)
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

    full_board = check_board(game_board)
    game_board_range = 100
    while full_board != True:  
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
                #displaying then checking board to see if there are any empty spaces left. DONE
                #if there are, keep playing and decrement the board range by 1. If not, game is automatically over. Display board. DONE
                if full_board == True:
                    break
                else:
                    game_board_range -= 1
                    continue
                
    print("The board is full. The game has ended. Thanks for playing!\n")

