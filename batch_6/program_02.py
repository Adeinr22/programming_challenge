# Prog02. removeprefix() remove the characters at the beginning of the string that matches the function parameter. 
# Create a program that do the same functionality without using removeprefix() function.
user_input = input("enter whatever you want: ")
user_remove = input("enter what you want to remove at the beginning: ")
final_output = ""
for char in user_input:
    if char == char in user_remove:
        pass
    else:
        final_output += char
print(final_output)