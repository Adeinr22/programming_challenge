# Prog08: Create a program that print all the odd numbers starting from 0 to 100. (Use while loop)
odd_checker = 0
while odd_checker != 100:
    odd_checker += 1
    if (odd_checker % 2) == 1:
        print(odd_checker)