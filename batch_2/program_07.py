# Prog07: Create a program that ask user to input 10 numbers. Print how many are even numbers.
even_counter = 0
for i in range(1,11):
    numbers_input = float(input(f"enter number {i}: "))
    if (numbers_input % 2) == 0:
        even_counter += 1
print(even_counter)