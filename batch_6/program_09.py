# Prog09. capitalize() makes the first letter of the string, capital letter. And all other letter in small case. 
# Create a program that do the same functionality without using capitalize() function.
user_input = input("enter whatever you want: ").lower()
capitalized_version = []
for char in user_input:
    if capitalized_version == []:
        capitalized_version.append(char.upper())
    else:
        capitalized_version.append(char)
        
for i in capitalized_version:
    print(i, end="")