number = int(input("enter a number "))

x = range(1, number+1)

for element in x:
    if number % element == 0:
        print("element " + str(element) + " is a divisor of the number")
    else:
        print("element " + str(element) + " is not a divisor of the number")
