# Prog08: Create a program that ask user to input 10 numbers. Print how many are odd numbers.
odd_counter = 0
for i in range(1,11):
    numbers_input = float(input(f"enter number {i}: "))
    if (numbers_input % 2) == 1:
        odd_counter += 1
print(odd_counter)