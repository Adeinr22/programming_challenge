# Prog05: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the average.
input_history = []
average = 0
try:
    while True:
        ask_user = float(input('enter a number: '))
        input_history.append(ask_user)
except:
    if input_history == []:
        print("invalid input and no number given")
    else:
        for i in input_history:
            average += i
        print(average / len(input_history))
