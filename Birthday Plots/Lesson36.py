from bokeh.plotting import figure, show, output_file
from collections import Counter
import json

def load_birthdays():
    with open("birthdays.json", "r") as f:
        birthday_info = json.load(f)

    print("Welcome to the birthday dictionary. We know the birthdays of:")

    {print(key) for key in birthday_info.keys()}

def add_birthdays(info_dict):
    scientist_name = input("What is the name you want to add?\n")
    scientist_birthday = input("What is the birthday of the scientist?\nPlease input as mm/dd/yyyy\n")
    with open("C:/Users/Bryce/Dropbox/Documents/Python lessons/Lesson34/birthdays.json", "r") as f:
        temp_birthday_info = json.load(f)

    temp_birthday_info[scientist_name] = scientist_birthday

    with open("C:/Users/Bryce/Dropbox/Documents/Python lessons/Lesson34/birthdays.json", "w") as f:
        json.dump(temp_birthday_info, f)
    
    with open("C:/Users/Bryce/Dropbox/Documents/Python lessons/Lesson34/birthdays.json", "r") as f:
        final_birthday_info = json.load(f)

    print("\n")
    print("Scientist birthdays:\n")
    return {print(key,value) for key,value in final_birthday_info.items()}

def decide_month(num_month, month_list):
    if num_month == 1:
        month = "January"
    elif num_month == 2:
        month = "February"
    elif num_month == 3:
        month = "March"
    elif num_month == 4:
        month = "April"
    elif num_month == 5:
        month = "May"
    elif num_month == 6:
        month = "June"
    elif num_month == 7:
        month = "July"
    elif num_month == 8:
        month = "August"
    elif num_month == 9:
        month = "September"
    elif num_month == 10:
        month = "October"
    elif num_month == 11:
        month = "November"
    elif num_month == 12:
        month = "December"
    month_list.append(month)

def count_birthdays():
    with open("C:/Users/Bryce/Dropbox/Documents/Python lessons/Lesson34/birthdays.json", "r") as f:
        birthday_info = json.load(f)
    
    #figure out loop to run through each scientist's birthday and count their month
    #can make each [:2] part of each string an integer
    #then depending on the number, assign a month string to another list "month list"
    #when loop is over, place the Counter(month_list)
    #then print the variable you save the counter in as a dictionary to display all the birthday counter
    month_list = []
    for b in birthday_info.values():
        temp = int(b[:2])
        decide_month(temp, month_list)
        
    c = Counter(month_list)
    print("Here is how many scientists' birthdays are in each month:")
    {print("{0}: {1}".format (month,num)) for month,num in c.items()}
    return c
    
def show_birthday_chart(birthday_dict):
    x_categories = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", " December"]
    month_list = []
    value_list = []
    for d in birthday_dict.keys():
        month_list.append(d)
    x = month_list
    
    for v in birthday_dict.values():
        value_list.append(v)
    y = value_list
    
    f = figure(x_range=x_categories)
    f.vbar(x=x, top=y, width=1.5)
    
    show(f)
    

if __name__ == "__main__":
    load_birthdays()
    birthday_lookup = input("Do you want to add a scientist's name and birthday? Yes or no?\n")
    if birthday_lookup == "no" or birthday_lookup == "No":
        print("okay, cya\n")
    elif birthday_lookup == "yes" or birthday_lookup == "Yes":
        birthday_info = {}
        add_birthdays(birthday_info)
    else:
        print("Can't allow any input besides yes or no, goodbye")

    var = count_birthdays()
    show_birthday_chart(var)