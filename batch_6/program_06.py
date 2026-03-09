# Prog06. ljust() add space characters at the end of the string to complete the number of characters specifies in function parameter. 
# Create a program that do the same functionality without using ljust() function.
try:
    user_input = input("enter whatever you want: ")
    width_input = int(input("What width do you want it to be (number): "))
    fill_input = input("what should you fill it with (must be single character): ")
    if len(user_input) < width_input:
        print(user_input)
    if len(fill_input) > 1:
        print("invalid input only a single character is allowed")
    else:
        for i in range(width_input - len(user_input)):
            user_input += fill_input
        print(user_input)
except:
    print("invalid input")