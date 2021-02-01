# from day 3-5 exercise - https://repl.it/@thakopian/day-3-5-exercise#main.py

'''
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

'''

# Write your code below this line 👇

# convert 2 inputs to lower case text
# add values of 2 inputs together into one string for counting
# count character values in the string
# match values to TRUE and LOVE in separate counts
# get totals for TRUE and LOVE
# combine each total into a new concatenated integer
# run that integer through logical operator ranges
# spell messages with the vlaue in it

# test with hard code values:

startSentence1 = 'Tadeh Hakopian'
startSentence2 = 'Britney Spears'
startSentence3 = startSentence1 + startSentence2
sentence = startSentence3.lower()

v1 = sentence.count('l')
v2 = sentence.count('o')
v3 = sentence.count('v')
v4 = sentence.count('e')

v5 = sentence.count('t')
v6 = sentence.count('r')
v7 = sentence.count('u')
v8 = sentence.count('e')


t1 = v1 + v2 + v3 + v4
t2 = v5 + v6 + v7 + v8

print(t1)
print(t2)

t3 = str(t1) + str(t2)

print(t3)

# either use the new concat strign for conditional logical statements or convert to integer if that doesn't work

if int(t3) < 10 or int(t3) > 90:
    print(f'your score {t3} does not fit')
elif int(t3) > 40 and int(t3) < 50:
    print(f'your score {t3} is ok')
else:
    print(f'your score {t3} does fit')

# this looks ok for the desired results
# apply the code to the input statements and use recursion to simplify it
