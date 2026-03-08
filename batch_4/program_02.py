# Prog02: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the number 
# with the most number of duplicate.
input_history = []
most_duplicates = None
duplicates_counter = 0
try:
    while True:
        ask_user = float(input('enter a number: '))
        input_history.append(ask_user)
except:
    if input_history == []:
        print("invalid input and no number given")
    else:
        for i in input_history:
            if input_history.count(i) > 1:
                if i > duplicates_counter:
                    duplicates_counter = input_history.count(i)
                    most_duplicates = i
            else:
                duplicates_checker = 'No duplicates'
                    
        if most_duplicates == None:
            print(duplicates_checker)
        else:
            print(most_duplicates)