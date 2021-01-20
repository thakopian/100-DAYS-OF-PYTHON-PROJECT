# https://repl.it/@thakopian/tip-calculator-start

# If the bill was $150.00, split between 5 people, with 12% tip.
# Each person should pay (150.00 / 5) * 1.12 = 33.6
# Format the result to 2 decimal places = 33.60
# Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
# HINT 1: https://www.google.com/search?q=how+to+round+number+to+2+decimal+places+python&oq=how+to+round+number+to+2+decimal
# HINT 2: https://www.kite.com/python/answers/how-to-limit-a-float-to-two-decimal-places-in-python

# input total bill, take input and ask for tip amount, then divide by number splitting bill, then provide that value in $ sing as float 2 decimals

##########################################
# my code below

# start with a message and input strings

print("Welcome to the tip calculator :]")

bill = input("what is the total bill?")

percent = input("what percentage would you like to give?")

split = input("how many people to split the bill?")

# convert the input strings to floats and integers

intBill = float(bill)
intPercent = float(percent)
intSplit = int(split)

# static test values below

# intBill = 122.33
# intPercent = 11
# intSplit = 7

# create a formula to get the bill split amount base on the values

pay = (intBill + (intBill * (intPercent/100))) / intSplit

# round the float to 2 decimal places per the prompt

payRound = round(pay, 2)

# use .format syntax to round the value to 0 places

payFinal = "{:.2f}".format(payRound)

# use fstrings to reply in print function what the split amount should be

print(f" Each person should pay ${payFinal}")
