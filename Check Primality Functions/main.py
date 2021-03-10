#program to determine if a number is prime or not
def get_number(number):
    return int(input(number))
   
def prime_or_nah(numb):
     x = range(2, numb - 1)
     last_element = x[-1]
     first_element = x[0]
     for element in x:
        if numb % element != 0 and element == last_element:
            print(str(numb) + " is a prime number")
        elif numb % element == 0:
            print(str(numb) + " is not a prime number")
            break
        elif numb % element != 0 and last_element == first_element:
            print(str(numb) + "is a prime number")
       
        

num = get_number("Give me a number: ")
prime_or_nah(num)


