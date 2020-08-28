# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 18:17:47 2020

@author: Bryce Benjamin
"""
#program takes a list of randomly generated numbers and gives the user 3 guesses to see if the user-given number exists in the random list.
# if user guesses the correct number, program stops and congratulate the user. If the user does not, program ends with a disappointing message.
#there are two ways: one way without binary search and one way using the binary search.


import random 

#function to find number in list without binary search
def find_num_in_list_nb(list_ex, num, exists):
    exists = num in list_ex
    if exists == True:
        print("{} exists in the list".format(num) )
    else:
        print("{} does not exist in the list".format(num) )

#function that will half the list to find the middle value
def halve_the_list(list1):
    try:
        middle_value = list1[int(len(list1)/2)]
        return middle_value
    except IndexError:
        print("number is out of range for list, start over.")
        
    
#function to find the number in list with binary search
def find_num_by_binary(list_ex, num, exists): 
    #will have to use a bool value that says if number was found, True or False 
    # If number has not been found, then it is false keep halving the list
    #if number has been found, then true and stop the program
    #take it one step at a time. FIRST make an algorithm and test it out step by step
    list_copy = list_ex.copy()
    print(list_copy)
    while len(list_copy) != 1:
        half = halve_the_list(list_copy)
       # print(half)
        if num < half:
            half_index = list_copy.index(half)
            list_copy = list_copy[ :half_index]
            
        elif num > half:
            half_index = list_copy.index(half)
            list_copy = list_copy[half_index:]
        else:
            exists = True
            return exists
        
    if len(list_copy) == 1:
        if num != list_copy[0]:
            exists = False
            return exists
        if num == list_copy[0]:
            exists = True
            
            return exists
    
   
    
if __name__ == "__main__":
    number_exists = False
    list1 = []
    guesses = 0
    for l in range(20):
        i = random.randint(0,20)
        if i in list1:
            continue
        else:
            list1.append(i)
    list1.sort()
    print(list1)
    
    #Example 1
    # find_num_in_list_nb(list1, number, number_exists)
    
    #Example 2
    while guesses < 3:
        number = input("Input a number to see if it exists in the list. You have 3 guesses: \n")
        number = int(number)
        number_exists = find_num_by_binary(list1, number, number_exists)
        if number_exists == False:
            guesses += 1
            print("number {:d} does not exist in the list".format(number))
            if guesses == 3:
                print("Guesses are all up! The correct number was: ", number)
                
        elif number_exists == True:
            print("number {:d} exists in the list".format(number) )
            break
       
        
        
        
    