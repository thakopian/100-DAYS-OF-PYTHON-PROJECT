# https://repl.it/@thakopian/day-4-1-exercise#README.md
# You are going to write a virtual coin toss program. It will randomly tell the user "Heads" or "Tails".
# the first letter should be capitalised and spelt exactly like in the example e.g. Heads, not heads.
# There are many ways of doing this. But to practice what we learnt in the last lesson, you should generate a random number, either 0 or 1. Then use that number to print out Heads or Tails.

# 1 means Heads
# 0 means Tails

# import the random module
import random

# create a value for random integers between 0 and 1
random_integer = random.randint(0, 1)

# check the number with a print
print(random_integer)

# use if statements to match 0 or 1 followed by the related text in print
if random_integer == 0:
    print('Tails')
if random_integer == 1:
    print('Heads')
