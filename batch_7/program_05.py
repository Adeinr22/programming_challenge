# Prog05. startswith() check if the string beginning part matches the function parameter. Create a program that 
# do the same functionality without using startswith() function.
user_input = input("enter whatever you want: ")
start_input = input("what should it start with: ")
checker = True
for i in range(len(start_input)):
    if user_input[i] != start_input[i]:
        checker = False

if checker:
    print(user_input + " starts with " + start_input)
else:
    print(user_input + " does not start with " + start_input)