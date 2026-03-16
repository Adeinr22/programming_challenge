# Prog02. removesuffix() remove the characters at the end of the string that matches the function parameter. Create a program 
# that do the same functionality without using removesuffix() function.
user_input = input("Enter whatever you want: ")
user_remove = input("Enter what you want to remove at the end: ")

if len(user_remove) <= len(user_input) and user_input[-len(user_remove):] == user_remove:
    result = user_input[:-len(user_remove)]
else:
    result = user_input

print(result)