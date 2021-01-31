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

if (calc / 4) % 2 == 0:
    print('leap year')
elif (calc / 100) % 2 == 0:
    print('not leap year')
else:
    print('leap year')
