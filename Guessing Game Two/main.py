#using binary search
#You, the user, will have in your head a number between 0 and 100. The program will guess a number, and you, the user, will say whether it is too high, too low, or your number.
#at end of exchange, program will print how many guesses it took to get my number

def calculate_mid(low, high):
    mid = int(low + ( (high - low) / 2))
    print("function returned mid as: {0}".format(mid))
    return mid

if __name__ == '__main__':
    lst1 = [i for i in range(101)]
    low, high = lst1[0], lst1[-1]
    mid = lst1[calculate_mid(low, high)] #function returns the corresponding middle value in the list between the lowest and highest number 
    is_guess_right = False 
    
    while is_guess_right == False:
        guess = str(mid)
        print("The algorithm has guessed this number: {0}".format(guess))
        correct_guess = str(input("Is this the correct number, yes or no?\n"))
        if correct_guess == "yes":
                is_guess_right = True
                break
        elif correct_guess == "no":
            higher_or_below = str(input("Is the number higher or lower than the guess?\n"))
            if higher_or_below == "higher":
                low = lst1[mid + 1] 
                mid = lst1[calculate_mid(low, high)]
                print("low is now {0} and high is now {1}".format(low, high))
                #leave high the same
                continue
            elif higher_or_below == "lower":
                high = lst1[mid - 1]
                mid = lst1[calculate_mid(low, high)]
                print("low is now {0} and high is now {1}".format(low, high))
                #mid = calculate_mid(low, high)
                #leave low the same
                continue
            else:
                print("Please input either higher or lower!")
                continue
        else:
            print("Say either yes or no please!")
            continue
    
    #done with loop, got the right guess. got here from the break in the inner if of the first try and except block.
    print("The algorithm has guessed the correct number, yerrr!!!")

        
