#This program asks the user how many Fibonnaci numbers to generate and then generates them

def get_number():
    number = int(input("Give me a number"))
    return number 

def generate_Fibonacci(size):
    #size = int(input("How many Fibonacci numbers to generate"))
    fibo = [1, 1]
    x = 1
    while x < size:
        fibo.append(fibo[x] + fibo[x - 1])
        x += 1

    print("fibonacci is " + str(fibo))
        

generate_Fibonacci(get_number())