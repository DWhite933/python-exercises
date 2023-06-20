# Write a program that, when run, greets the user by printing “Hello, world!” on the screen. 
# Then it prints a message on the screen asking the user to enter their name. The program greets the user by name by printing the 
# “Hello,” followed by the user’s name.
# Let’s use “Alice” as the example name. Your program’s output should look like this:
#   Hello, world!
#   What is your name?
#   Alice
#   Hello, Alice

# print hello world
print('Hello, world!')

# ask user for name
print('What is your name?')

# get  user's name from keybord input
name = input()

# greet user by their name
print(f'Hello, {name}!')