# Prog07. zfill() add zero characters at the beginning of the string to complete the number of characters specifies 
# in function parameter. Create a program that do the same functionality without using zfill() function.
try:
    user_input = input("Enter whatever you want: ")
    width_input = int(input("What width do you want it to be (number): "))

    if width_input < 0:
        print(user_input)
    elif len(user_input) < width_input:
        zeros_needed = width_input - len(user_input)
        zeros = '0' * zeros_needed 
        if user_input[0] == '+':
            print('+' + zeros + user_input[1:])
        elif user_input[0] == '-':
            print('-' + zeros + user_input[1:])
        else:
            print(zeros + user_input)
    else:
        print(user_input)

except:
    print("Invalid input")