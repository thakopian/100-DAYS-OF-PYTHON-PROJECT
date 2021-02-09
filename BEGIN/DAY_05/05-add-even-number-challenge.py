# https://repl.it/@thakopian/day-5-3-exercise#main.py

#  calculate sum of all even numbers from 1 to 100
# only one print statement

'''
# add all values from 1 to 100
total = 0
for x in range(1, 101):
    total += x
print(total)
'''

# check your values by printing the range using a step value first
for x in range(0, 101, 2):
    print(x)

# use the correct even numbers to add everything up
# note can also start from 2 b/c 0 does not add anything to the total
total = 0
for x in range(0, 101, 2):
    total += x
print(total)
