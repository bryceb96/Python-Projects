#program will determinea strong or weak password for a user
import random


list_of_password_objects = []

def listToString(s):
    return ("".join(s))

def make_password(main_list):
    i = 0
    #limit = 3
    count = 0
    number_list = ['1','2','3','4','5','6','7','8','9']
    char_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'j', 'k', 'q', 'z', 'X', 'B', 'A', 'F', 'R', 'T', 'P', 'L', 'Q', 'Z', 'M', 'D']
    symbol_list = ['#', '%', '&', '@', '*', '(', '^', '{', '!', '$', '>', '<']
    word_list = ['red', 'blue']
    limit_set = int(input("how many characters do you want the password to be at minimum?\nMust be bigger than 0\n"))
    while limit_set == 0:
        print("number must be bigger than 0")
        limit_set = int(input("how many characters do you want the password to be at minimum? Must be bigger than 0\n"))
        if limit_set > 0:
            break

    password_strength = str(input("how strong do you want the password? \nstrong or weak?\n"))
    if password_strength == "strong":
        while count < limit_set:
            random.shuffle(number_list)
            random.shuffle(char_list)
            random.shuffle(symbol_list)
            main_list.append(number_list[i])
            count += 1
            if count == limit_set:
                break
            main_list.append(char_list[i])
            count += 1
            if count == limit_set:
                break
            main_list.append(symbol_list[i])
            count += 1
            if count == limit_set:
                break
            #i += 1
        listToString(main_list)

    elif password_strength == "weak":
        while count < 2:
            random.shuffle(word_list)
            main_list.append(word_list[i])
            main_list.append(str(count))
            count += 1
            if count == limit_set:
                break
        listToString(main_list)
    else:
        print("please choose a strong or weak option")
        make_password(main_list)

    return main_list

user_input = str(input("Do you want a new password, yes or no?\n"))
while user_input != "no":
    list_of_password_objects = []
    make_password(list_of_password_objects)
    print("here is your new password:", "".join(list_of_password_objects))
    user_input = str(input("do you want a new password? yes or no?\n"))
        
    

        

