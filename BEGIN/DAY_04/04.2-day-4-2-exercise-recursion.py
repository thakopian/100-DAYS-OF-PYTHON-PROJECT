# https://repl.it/@thakopian/day-4-2-exercise#main.py
# this time use the random.choice() function
# inputs for the names - Angela, Ben, Jenny, Michael, Chloe

# import modules
import random

# input function
names_string = input("Give me everybody's names, separated by a comma. ")
# split the strings to spearate the values by comma
names = names_string.split(", ")
# use the random choice function to randomize the names variable stored values
person_who_pays = random.choice(names)
# print the result
print(person_who_pays + " is going to buy the meal today")
