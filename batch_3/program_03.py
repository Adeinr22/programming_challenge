# Prog03: Create a program that ask user to input a number, continue asking until the user input is invalid. Display "Unique" after input
# when the inputted number don't have duplicate. Display "Duplicate" after input when the inputted number have duplicate.
input_history = []
try:
    while True:
        ask_user = float(input('enter a number: '))
        if ask_user not in input_history or input_history == []:
            print('Unique')
            input_history.append(ask_user)
        else:
            print('Duplicate')
except:
    print("invalid input") 