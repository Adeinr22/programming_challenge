# Prog06. rjust() add space characters at the beginning of the string to complete the number of characters specifies 
# in function parameter. Create a program that do the same functionality without using rjust() function.
try:
    user_input = input("Enter whatever you want: ")
    width_input = int(input("What width do you want it to be (number): "))
    fill_input = input("What should you fill it with (must be a single character): ")

    if len(fill_input) == 0:
        fill_input = " "
    elif len(fill_input) > 1:
        print("The fill character must be exactly one character")
    if width_input <= len(user_input) and len(fill_input) == 1:
        result = user_input
        print(result)
    elif len(fill_input) == 1:
        result = fill_input * (width_input - len(user_input)) + user_input
        print(result)

except ValueError:
    print("Invalid input: width must be an integer.")