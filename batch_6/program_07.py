# Prog07. center() add space characters at the beginning and at the end of the string to print the string at the center. Create a 
# program that do the same functionality without using center() function.
try:
    user_input = input("Enter whatever you want: ")
    width_input = int(input("What width do you want it to be (number): "))
    fill_input = input("What should you fill it with (must be a single character): ")

    if len(fill_input) != 1:
        print("Error: fill character must be exactly one character.")
        import sys
        sys.exit(1)

    if width_input <= len(user_input):
        result = user_input
    else:
        total_padding = width_input - len(user_input)
        left_padding = total_padding // 2          
        right_padding = total_padding - left_padding 
        result = fill_input * left_padding + user_input + fill_input * right_padding

    print(result)

except ValueError:
    print("Invalid input: width must be an integer.")