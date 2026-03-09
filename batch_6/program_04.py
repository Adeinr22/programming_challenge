# Prog04. isupper() check if all characters of the string is on upper case. Create a program that do the same functionality without using isupper() function.

user_input = input("enter whatever you want: ")
lower_checker = False
temu_isupper = False
for char in user_input:
    if char == char.lower() and char != " ":
        lower_checker = True
    else:
        pass
if lower_checker:
    pass
else:
    temu_isupper = True
if temu_isupper:
    print("all characters are uppercase")
else:
    print("input contains a lowercase")
