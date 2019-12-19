#program to learn the conditionals and the comparators of Python

number = int(input("give me a number "))
if number % 2 == 0:
    print("even number")
elif number % 4 == 0:
    print("multiple of 4")
else:
    print("odd number")

num = int(input("\ngive me another number "))
check = int(input("\ngive me another number to divide by "))
if num % check == 0:
    print("check divides evenly into num")
else:
    print("check does not divide evenly into num")
