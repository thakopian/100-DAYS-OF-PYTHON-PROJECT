# leap year calculator challenge
# hints in day3/002 modulo BMI calculator

# https://repl.it/@thakopian/day-3-3-exercise#README.md

calc = int(input("Which year do you want to check? "))

#calc = year % 4

# print(calc)

'''

if calc % 4 == 0:
    print('leap year')
    if calc % 100 == 0:
        print('not leap year')
    else:
        print('leap year')

'''
'''
if calc % 4 == 0:
    print('leap year')
elif calc % 100 == 0:
    print('not leap year')
else:
    print('leap year')
'''
# I can make the year run through the first condition but can't pass it to the next one. I am missing some step here either in math or conditional nesting

'''

if (calc / 4) % 2 == 0:
    print('leap year')
elif (calc / 100) % 2 == 0:
    print('not leap year')
else:
    print('leap year')

'''

# rewrite the calculations with modulo only, no divisions
# you are going through conditional statements to find if the REMAINDER meets your criteria not the actual division

# long version with nested if statements and format text

if (calc % 4) == 0:
    if (calc % 100) == 0:
        if (calc % 400) == 0:
            print("{0} is a leap year".format(calc))
        else:
            print("{0} is not a leap year".format(calc))
    else:
        print("{0} is  a leap year".format(calc))
else:
    print("{0} is not a leap year".format(calc))
