my_list = [1, 2, 3, 4, 4, 5, 6, 7, 8, 10, 13, 21, 34, 55, 89]
other_list = []
#for element in my_list:
    #other_list = []
    #if element < 5:
     #   other_list.append(element)
    
number = int(input("Enter a number "))


for element in my_list:
    if element < number:
        other_list.append(element)

for word in other_list:
    print(word)