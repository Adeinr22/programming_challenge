# Prog02. removesuffix() remove the characters at the end of the string that matches the function parameter. Create a program 
# that do the same functionality without using removesuffix() function.
user_input = input("enter whatever you want: ")
user_remove = input("enter what you want to remove at the end: ")
final_output = []
for char in user_input:
    final_output.append(char)
for i in range(len(user_remove), -1, -1):
    if user_remove[i - 1] == final_output[-1]:
        final_output.pop()
for i in final_output:
    print(i, end="")