#program to generate two random lists and find the common elements in both lists
import random

a = random.sample(range(1,50), 10)
b = random.sample(range(1,50), 10)
c = []


for x in a:
    for y in b:
        if x == y:
            c.append(x)
        

for element in c:
    print(element)