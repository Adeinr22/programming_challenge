# Prog07. center() add space characters at the beginning and at the end of the string to print the string at the center. Create a 
# program that do the same functionality without using center() function.
try:
    user_input = input("enter whatever you want: ")
    width_input = int(input("What width do you want it to be (number): "))
    fill_input = input("what should you fill it with (must be single character): ")
    if len(user_input) < width_input:
        print(user_input)

    if len(fill_input) > 1:
        print("invalid input only a single character is allowed")
        
    if fill_input == '':
        for i in range(int((width_input - len(user_input)) / 2)):
            user_input = user_input + " "
            user_input = " "+ user_input 
        print(user_input)
        
    if len(fill_input) == 1 and fill_input != '':
        for i in range(int((width_input - len(user_input)) / 2)):
            user_input = user_input + fill_input
            user_input = fill_input + user_input 
        print(user_input)
except:
    print("invalid input")