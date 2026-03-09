# Prog04. islower() check if all characters of the string is on lower case. Create a program that do the same 
# functionality without using islower() function.
user_input = input("enter whatever you want: ")
upper_checker = False
temu_islower = False
for char in user_input:
    if char == char.upper() and char != " ":
        upper_checker = True
    else:
        pass
if upper_checker:
    pass
else:
    temu_islower = True
if temu_islower:
    print("all characters are lowercase")
else:
    print("input contains a uppercase")
