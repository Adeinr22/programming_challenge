# Prog05. endswith() check if the string end part matches the function parameter. Create a program that do the same 
# functionality without using endswith() function.
user_input = input("enter whatever you want: ")
end_input = input("what should it end with: ")
checker = True
if len(end_input) > len(user_input):
    checker = False
else:
    for i in range(len(end_input)):
        if user_input[(-1 - i)] != end_input[(-1 - i)]:
            checker = False
            break

if checker:
    print(user_input + " ends with " + end_input)
else:
    print(user_input + " does not end with " + end_input)