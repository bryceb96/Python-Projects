import random

ulist = []
def TakeList(example):
    i = 0
    total = 25
    while i < total:
        example.append(random.randint(1,10))
        i += 1
    #random.sample(range(1,10), 5)
    print("The list is: " + str(example))
   

def TakeSet(example):
    example = set(example)
    print("The list is now a set: " + str(example))

TakeList(ulist)
TakeSet(ulist)