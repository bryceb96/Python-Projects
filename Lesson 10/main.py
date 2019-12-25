import random

a = random.sample(range(1,50), 20)
b = random.sample(range(1,50), 20)
c = [num for num in a for ele in b if num == ele]

for x in c:
    if x == x + 1:
        c.remove(x + 1)
        print(x)
    else:
        print(x)
    