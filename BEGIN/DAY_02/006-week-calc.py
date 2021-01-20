# https://repl.it/@thakopian/day-2-3-exercise
# use math and f-strings to list how many days, weeks and months we have until we are 90 years old based on your current age


age = input("What is your current age?")

# take age and subtract it from 90 to get remaining time

nAge = 90 - int(age)
print(nAge)

# use remaining time to multiply by the date formats

month = nAge * 12
week = nAge * 52
day = nAge * 365

# use date formats in an f-string to create a message

print(f"you have {day} days, {week} weeks, and {month} months left to live")
