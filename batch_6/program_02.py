# Prog02. removeprefix() remove the characters at the beginning of the string that matches the function parameter. 
# Create a program that do the same functionality without using removeprefix() function.
user_input = input("enter whatever you want: ")
user_remove = input("enter what you want to remove at the beginning: ")
final_output = []
for char in user_input:
    final_output.append(char)
for char in user_remove:
    if char == final_output[0]:
        final_output.pop(0)
for i in final_output:
    print(i, end="")