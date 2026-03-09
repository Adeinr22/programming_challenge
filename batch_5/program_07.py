# Prog07: Create a program that ask the user to input a complete statement. Print the number of words in the input.
user_statement = input("enter a complete statement: ")
words_list = user_statement.split()
word_counter = len(words_list)
print(word_counter)