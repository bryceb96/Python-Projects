word = str(input("please enter a word "))

a = []
b = []

for x in word:
    a.append(x)

reverse = str(word[::-1])
for y in reverse:
    b.append(y)


if reverse == word:
    print("this word is a palindrome")
else:
    print("this word is not a palindrome")