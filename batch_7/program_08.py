# count() return how many time the function parameter appear in the string. Create a program that do the 
# same functionality without using count() function.
user_input = input("enter whatever you like: ")
count_input = input("what would you like to count: ")
counter = 0

if count_input == "":
    print("Error: empty substring")
else:
    i = 0
    while i <= len(user_input) - len(count_input):
        if user_input[i:i+(len(count_input))] == count_input:
            counter += 1
            i += len(count_input)
        else:
            i += 1

print(f'there are {counter} of ' + count_input)