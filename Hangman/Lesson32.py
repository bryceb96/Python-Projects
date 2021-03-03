'''
This is a game of Hangman.
Player only has 6 guesses to guess the right word. The word is picked from a random word list and the player must guess the word.
The game will keep track of incorrectly guessed letters and if a letter is guessed right, program will output the current correctly guessed word without counting the number of incorrect guesses.
Enjoy! :)

'''
import random

def pick_word(txt_file): #function picks a random word for the user to guess against

    with open(txt_file, 'r') as f:
        lines = f.readlines()
    return(random.choice(lines))

def make_list(word): #function makes the list that will contain the correct guesses of by the user
    word = word.rstrip()
    copy = []
    for i in range(len(word)):
        copy.append("_")
        
    return(copy)

def match_user_guess(guess, word, list1): # function will see if the user inputted guess is correct or not
    correct_letter = False
    guess = guess.upper()
    if guess in word:
        for i in range(len(word)):
            if word[i] == guess: #matches indices of list to guess if present
                pos = i
                list1[pos] = guess
                correct_letter = True
        new_word = "".join(list1)
        print(new_word)
        return correct_letter
    else:
        if guess.isspace() == True:
            print(guess.isspace())
            print("please input a character not just whitespace")
            correct_letter = True
            return correct_letter
        else:
            print("incorrect!")
            new_word = "".join(list1)
            print(new_word)
            return correct_letter
        
    

def check_input(guess): #function validates the input by the user
    if len(guess) > 1 or len(guess) == 0 or type(guess) is not str or guess.isspace() == True:
        print("please input only one character please.")

def play_again():
    while 1==1:
        play_again = input("Do you want to play again, type yes or no\n")
                
        if play_again == "yes":
            lets_play = True
            break
        elif play_again == "no":
            lets_play = False
            break
        else:
            print("Please input yes or no.")
    return lets_play

'''
def store_user_guesses(guess):
    guess_set = set()
    guess_set.add(guess)
    print("You have guessed these letters: {0} ".format(guess_set))
'''  
    
if __name__== "__main__":
    lets_play = True
    while lets_play == True:
        guess_count = 0
        correct_word = False
        correct_letter = False
        word = pick_word('sowpods.txt')
        guess_list = make_list(word)
        print(guess_list)
        underscore = "_" #how the places in the guess list will look before the user guesses the correct letter 
        guess_set = set()
        
        while underscore in guess_list:
            guess = input("Guess your letter in all caps: \n") 
            check_input(guess)
            #print(word)
            correct_letter = match_user_guess(guess, word, guess_list)
            print(word)
            
            guess_set.add(guess)
            print("You have guessed these letters: {0} ".format(guess_set))
            
            if guess_count < 6 and correct_letter == False:
                print("you have {0} guesses left".format(6 - guess_count))
                guess_count += 1
                
            elif correct_letter == True and guess_count < 6:
                guess_count = guess_count
                
        
            elif guess_count == 6:
                print("you are out of guesses. Game over.")
                print("the correct word was {0}".format(word))
                lets_play = play_again()
                break
            
       
        if underscore not in guess_list and guess_count < 6:
            correct_word = True     
            print("Congrats, you guessed the right word!")
            print("You had {0} incorrect guesses.".format(guess_count))
            lets_play = play_again()
            
            
        