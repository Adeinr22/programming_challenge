user_input = input("enter whatever you want: ")
lower_checker = False
for char in user_input:
    if "a" <= char <= "z":
        lower_checker = True
    else:
        pass
if user_input == str(int(user_input)):
    print("No uppercase")
else:
    if lower_checker:
        print("input contains a lowercase")
    else:
        print("all characters are uppercase")