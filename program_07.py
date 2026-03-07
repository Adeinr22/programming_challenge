# Prog07: Create a program that ask user to input 10 numbers. Print the sum of all the numbers.
numbers_sum = 0
for i in range(1,11):
    numbers_input = float(input(f"enter number {i}: "))
    numbers_sum += numbers_input
print(numbers_sum)