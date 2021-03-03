import random 
#program will have user guess the correct numbers in a random number. if the place of the number is guessed in the right place, it is a cow.
#if a number is in the random number but in the wrong place, then it is a bull.
# if a number does not exist in the random number, then it is neither a bull or a cow.
#once there are 4 cows, then the program ends.
print("Welcome to the Cows and Bulls game!")
def generate_random_number():
        number = random.randint(1000,9999)
        return number

def read_the_numbers():
        number_to_guess = generate_random_number()
        cow_count = 0
        bull_count = 0
        guessCount = 0
        while cow_count != 4:
            user_num = input("Guess the random number: ")
                    #checking that user input is 4 numbers long
            guessCount += 1
            if len(user_num) > 4 and len(user_num) < 4: 
                print("Enter a number that is 4 numbers long")
                break
            
            #turn numbers to strings so they will become lists
            watch_number = str(number_to_guess)
            
            #print(user_input)

            given_number1 = watch_number[0]
            given_number2 = watch_number[1]
            given_number3 = watch_number[2]
            given_number4 = watch_number[3]

            user_num1 = user_num[0]
            user_num2 = user_num[1]
            user_num3 = user_num[2]
            user_num4 = user_num[3]
            
            #this was for testing to see what the user number was and the random number was.
            # helped me with figuring out to implement the program 
            '''
            print("index 1 of user number", user_num1)
            print("index 2 of user number", user_num2)
            print("index 3 of user number", user_num3)
            print("index 4 of user number", user_num4)

            print("index 1 of given number", given_number1)
            print("index 2 of given number", given_number2)
            print("index 3 of given number", given_number3)
            print("index 4 of given number", given_number4)
            '''

            if user_num1 == given_number1:
                cow_count += 1
            # print("\ncow count is: ", cow_count)
            elif user_num1 != given_number1 and user_num1 == given_number2 or user_num1 == given_number3 or user_num1 == given_number4:
                bull_count += 1
                #print("\nbull count is: ", bull_count)
            if user_num2 == given_number2:
                cow_count += 1
                #print("\ncow count is: ", cow_count)
            elif user_num2 != given_number2 and user_num2 == given_number1 or user_num2 == given_number3 or user_num2 == given_number4:
                bull_count += 1
                #print("\nbull count is: ", bull_count)
            if user_num3 == given_number3:
                cow_count += 1
                #print("\ncow count is: ", cow_count)
            elif user_num3 != given_number3 and user_num3 == given_number1 or user_num3 == given_number2 or user_num3 == given_number4:
                bull_count += 1
                #print("\nbull count is: ", bull_count)
            if user_num4 == given_number4:
                cow_count += 1
                #print("\ncow count is: ", cow_count)
            elif user_num4 != given_number4 and user_num4 == given_number1 or user_num4 == given_number2 or user_num4 == given_number3:
                bull_count += 1
                #print("\nbull count is: ", bull_count)
            
            print("\ncow count is: ", cow_count)
            print("\nbull count is: ", bull_count)

            if cow_count == 4:
                print("You took this many guesses: ", guessCount)
                print("thank you for playing the game.")
                break
            else:
                cow_count = 0
                bull_count = 0
                continue 
            
            #cow_count = 0
            #bull_count = 0


if __name__=="__main__":
    read_the_numbers()