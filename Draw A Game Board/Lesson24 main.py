#Program draws a game board

def create_horizontal_graphic(num1):
    horizontal_sym = " ---" * num1
    print(horizontal_sym)

def create_vertical_graphic(num1):
    vertical_sym = "|   " * (num1 + 1)
    print(vertical_sym)

user_num = int(input("What board size you want fam? \n"))

for i in range(user_num):
    create_horizontal_graphic(user_num)
    create_vertical_graphic(user_num)
print(" ---" * user_num)


