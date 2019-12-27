#program to output the first and last elements of a randomly generated list
import random

def get_list():
    a = random.sample(range(1,50), 7)
    print(a)
    return print("first and last elements of a list are: " + str(a[0]) + " and " + str(a[-1]))


get_list()





