#program will print the user given word backwards
def repeat_word_backward():
    word = str(input("enter a long string of words please: "))
    print(word)
    word = word.split()
    word.reverse()
    word = " ".join(word)
    print("The new reversed list is: ", word)

repeat_word_backward()
