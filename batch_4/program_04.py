# Prog04: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the number 
# from highest to lowest. Clue: sort() function
input_history = []
try:
    while True:
        ask_user = float(input('enter a number: '))
        input_history.append(ask_user)
except:
    if input_history == []:
        print("invalid input and no number given")
    else:
        input_history.sort(reverse=True)
        print(input_history)