# https://repl.it/@thakopian/day-4-2-exercise#main.py

# write a program which will select a random name from a list of names
# name selected will pay for everyone's bill

# cannot use choice() function

# you may need the split() and len() function with the random module for this code
# list starts at index 0

# Split string method
import random

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

# len() for getting the value in the range of x number of names you put in
print(len(names))

random_name = random.randint(0, 4)

print(random_name)

# my solution did not work because the len is not contributing to the random value generator
# I need to lace len into the random generator while accounting for the index 0 of the list
