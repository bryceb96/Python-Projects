import numpy as np
#program tells us the winner of the tic tac toe game. 0 is empty square, 1 is player 1, and 2 is player 2

def determine_winner(matrix):
    for i in range(0,3):
        if matrix[i][0] == matrix[i][1] == matrix[i][2]:
            if matrix[i][0] == 1:
                print("player 1 wins horizontally")
                break
            elif matrix[i][0] == 2:
                print("player 2 wins horizontally")
                break
            else:
                print("there is no winner")
            break
        #checking horizontal columns
        elif matrix[0][i] == matrix[1][i] == matrix[2][i]:
            if matrix[0][i] == 1:
                print("player 1 wins vertically")
                break
            elif matrix[0][i] == 2:
                print("player 2 wins vertically")
                break
            else:
                print("there is no winner")
            break
        #checking diagonally
        elif matrix[0][0] == 2 and matrix[1][1] == 2 and matrix[2][2] == 2 or matrix[0][2] == 2 and matrix[1][1] == 2 and matrix[2][0] == 2:
            print("player 2 wins diagonally")
            break
        elif matrix[0][0] == 1 and matrix[1][1] == 1 and matrix[2][2] == 1 or matrix[0][2] == 1 and matrix[1][1] == 1 and matrix[2][0] == 1:
            print("player 1 wins diagonally")
            break
    else:
       print("there is no winner")
            
if __name__ == "__main__":

    winner_is_2 = [[2, 2, 0],
        [2, 1, 0],
        [2, 1, 1]]

    winner_is_1 = [[1, 2, 0],
        [2, 1, 0],
        [2, 1, 1]]
    
    winner_is_also_1 = [[0, 1, 0],
        [2, 1, 0],
        [2, 1, 1]]

    no_winner = [[1, 2, 0],
        [2, 1, 0],
        [2, 1, 2]]

    also_no_winner = [[1, 2, 0],
        [2, 1, 0],
        [2, 1, 0]]

    determine_winner(winner_is_2)
    determine_winner(winner_is_1)
    determine_winner(winner_is_also_1)
    determine_winner(no_winner)
    determine_winner(also_no_winner)
    

    
    
