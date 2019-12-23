#program to have user guess a random number between 1 and 10
import random
num = random.randint(1,10)
num = str(num)
flag = False
#guess = str(input("Guess a number between 1 and 9 "))
while flag == False:
    guess = str(input("Guess a number between 1 and 10 "))
   
    if guess == num:
        flag == True
        print("You guessed the right number!")
        break
    else:
        print("You did not guess the right number, try again")
        flag == False
        continue

