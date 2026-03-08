# Prog03: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the highest number
input_history = []
try:
    while True:
        ask_user = float(input('enter a number: '))
        input_history.append(ask_user)
except:
    if input_history == []:
        print("invalid input and no number given")
    else:
        print(max(input_history))